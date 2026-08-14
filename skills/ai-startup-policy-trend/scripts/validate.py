#!/usr/bin/env python3
"""ai-startup-policy-trend 技能验证脚本。

断言"产出=合规成立"而非"动作已执行"：
- GOOD 样例：含全部合规要素，且无违规 → exit 0
- BAD 样例：命中任一违规模式 → exit 1

退出码契约：0=通过，1=存在错误，2=文件错误。
"""
import re
import sys
from pathlib import Path

EXIT_OK = 0
EXIT_FAIL = 1
EXIT_FILE_ERROR = 2


def read_sample(path: str) -> str:
    p = Path(path)
    if not p.is_file():
        print(f"文件不存在: {path}", file=sys.stderr)
        sys.exit(EXIT_FILE_ERROR)
    return p.read_text(encoding="utf-8")


GOOD_REQUIREMENTS = [
    ('备案|算法备案|生成式', '缺少备案义务判定（双备案）'),
    ('数据出境|安全评估|标准合同|认证', '缺少数据出境路径判断'),
    ('(欧盟|EU).{0,6}AI Act|境外.{0,4}(法规|适用)', '缺少境外 AI 法规适用判断'),
    ('阈值|人数|敏感', '缺少阈值/敏感数据判定'),
    ('gotchas|坑位|红线', '缺少 gotchas 坑位引用'),
]

BAD_VIOLATIONS = [
    ('(无需|不用|免).{0,4}(备案|登记).{0,8}(直接)?(上线|上线|发布|服务)', '命中违规：不备案直接上线'),
    ('(数据|个人信息).{0,8}(随便|随意|直接).{0,4}(出境|传出|传到境外)', '命中违规：数据随意出境'),
    ('(境外|国外|美国|欧盟).{0,8}(没有|无).{0,4}(AI )?(法规|法律|监管)', '命中违规：境外无 AI 法幻觉'),
    ('先(上线|发布|跑).{0,6}(后|再).{0,4}(补|备案)', '命中违规：先上线后备案'),
]


def find_violations(text: str) -> list:
    hits = []
    for pattern, msg in BAD_VIOLATIONS:
        if re.search(pattern, text, re.IGNORECASE):
            hits.append(msg)
    return hits


def find_missing_good(text: str) -> list:
    missing = []
    for pattern, msg in GOOD_REQUIREMENTS:
        if not re.search(pattern, text, re.IGNORECASE):
            missing.append(msg)
    return missing


def main():
    if len(sys.argv) < 2:
        print("用法: validate.py <sample.md>", file=sys.stderr)
        sys.exit(EXIT_FILE_ERROR)

    sample_path = sys.argv[1]
    text = read_sample(sample_path)
    fname = Path(sample_path).name.lower()
    is_bad = "bad" in fname

    errors = []

    violations = find_violations(text)
    if is_bad:
        if not violations:
            errors.append("BAD 样例未命中任何已知违规模式（应至少命中一条）")
        else:
            errors.append(f"BAD 样例命中 {len(violations)} 条违规（预期失败）：{'; '.join(violations)}")
    else:
        if violations:
            errors.append(f"GOOD 样例命中违规（不应有）：{'; '.join(violations)}")
        missing = find_missing_good(text)
        errors.extend(missing)

    if errors:
        print(f"验证失败（{len(errors)} 项）：", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(EXIT_FAIL)

    print("验证通过")
    sys.exit(EXIT_OK)


if __name__ == "__main__":
    main()
