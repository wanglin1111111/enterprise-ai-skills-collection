#!/usr/bin/env python3
"""
Enterprise AI Skills Collection - Quick Fix Script
修复P0级问题:
1. 技能文件在根目录 -> 移动到 skills/ 目录
2. 缺少metadata.json -> 创建
3. 缺少全局索引 -> 创建 INDEX.md
4. 技能数量声明不符 -> 修正README
"""

import os
import shutil
from pathlib import Path

def create_directory_structure():
    """创建标准目录结构"""
    print("[1/5] Creating standard directory structure...")
    
    dirs = [
        "skills/ai-driven-economic-research",
        "skills/ai-driven-economic-research/test",
        "skills/ai-driven-economic-research/example"
    ]
    
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
        print(f"  Created: {d}/")
    
    print()

def move_skill_files():
    """移动技能文件到标准位置"""
    print("[2/5] Moving skill files to standard location...")
    
    moves = [
        ("SKILL.md", "skills/ai-driven-economic-research/SKILL.md"),
        ("QUICKREF.md", "skills/ai-driven-economic-research/QUICKREF.md"),
        ("TEST.md", "skills/ai-driven-economic-research/test/test_cases.md")
    ]
    
    for src, dst in moves:
        if Path(src).exists():
            shutil.move(src, dst)
            print(f"  Moved: {src} -> {dst}")
        else:
            print(f"  [WARN] Not found: {src}")
    
    print()

def create_root_metadata():
    """创建根目录metadata.json"""
    print("[3/5] Creating root metadata.json...")
    
    metadata = """{
  "name": "enterprise-ai-skills-collection",
  "version": "1.0.0",
  "description": "企业AI应用技能集合 - 统一仓库",
  "repository": "https://github.com/wanglin1111111/enterprise-ai-skills-collection",
  "author": "wanglin1111111",
  "license": "MIT",
  "skills_count": 1,
  "skills": [
    {
      "name": "ai-driven-economic-research",
      "description": "AI技术在经济学研究中的系统化应用框架",
      "category": "research",
      "test_score": 89.8,
      "test_grade": "A",
      "path": "skills/ai-driven-economic-research/"
    }
  ],
  "created_at": "2026-05-25",
  "updated_at": "2026-05-29"
}
"""
    
    with open("metadata.json", "w", encoding="utf-8") as f:
        f.write(metadata)
    
    print("  Created: metadata.json")
    print()

def create_skill_metadata():
    """创建技能级metadata.json"""
    print("[4/5] Creating skill-level metadata.json...")
    
    metadata = """{
  "name": "ai-driven-economic-research",
  "version": "1.0.0",
  "description": "AI技术在经济学研究中的系统化应用框架，涵盖非传统数据处理、预测分析方法、跨学科融合研究、就业影响评估四大核心模块",
  "category": "research",
  "author": "wanglin1111111",
  "license": "MIT",
  "keywords": [
    "economics",
    "ai-research",
    "text-analysis",
    "image-analysis",
    "forecasting",
    "policy-analysis",
    "employment-impact"
  ],
  "test_score": 89.8,
  "test_grade": "A",
  "created_at": "2026-05-25",
  "updated_at": "2026-05-29",
  "files": [
    "SKILL.md",
    "QUICKREF.md",
    "test/test_cases.md"
  ]
}
"""
    
    with open("skills/ai-driven-economic-research/metadata.json", "w", encoding="utf-8") as f:
        f.write(metadata)
    
    print("  Created: skills/ai-driven-economic-research/metadata.json")
    print()

def create_index():
    """创建全局索引INDEX.md"""
    print("[5/5] Creating global index INDEX.md...")
    
    index = """# Enterprise AI Skills Collection

> 企业AI应用技能集合 - 统一仓库

## 技能列表

| 技能名称 | 描述 | 测试得分 | 状态 |
|----------|------|----------|------|
| [AI驱动的经济学研究](skills/ai-driven-economic-research/) | AI技术在经济学研究中的系统化应用框架 | 89.8/100 (A) | ✅ 可用 |

## 技能详情

### AI驱动的经济学研究 (ai-driven-economic-research)

- **描述**: AI技术在经济学研究中的系统化应用框架
- **核心内容**: 文本数据分析、图像数据应用、预测方法融合、就业影响评估
- **测试得分**: 89.8/100 (A)
- **文件位置**: [skills/ai-driven-economic-research/](skills/ai-driven-economic-research/)
- **适用人群**: 经济研究人员、数据科学家、政策分析师、社会科学研究者

#### 核心模块

1. **文本数据量化分析**
   - 主题提取、情感分析、文本分类
   - 政府报告、会议纪要、历史文献分析

2. **图像数据应用**
   - 卫星图像、街景图像、医疗影像分析
   - 物体识别、场景分析、变化检测

3. **预测方法融合**
   - 经济指标预测、市场趋势分析
   - 机器学习预测模型、因果推断

4. **就业影响评估**
   - 就业结构分析、收入分配研究
   - AI对劳动力市场的影响评估

## 目录结构

```
enterprise-ai-skills-collection/
├── metadata.json                    # 全局元数据
├── README.md                        # 项目说明
├── INDEX.md                         # 技能索引（本文件）
└── skills/
    └── ai-driven-economic-research/   # 技能目录
        ├── SKILL.md                   # 技能文档
        ├── QUICKREF.md                # 快速参考
        ├── metadata.json              # 技能元数据
        ├── test/
        │   └── test_cases.md          # 测试用例
        └── example/
            └── real_world_examples.md # 使用示例
```

## 使用方式

### 查看技能详情

```bash
# 阅读完整技能文档
cat skills/ai-driven-economic-research/SKILL.md

# 查看快速参考
cat skills/ai-driven-economic-research/QUICKREF.md

# 查看测试用例
cat skills/ai-driven-economic-research/test/test_cases.md
```

### 安装技能

```bash
# 克隆仓库
git clone https://github.com/wanglin1111111/enterprise-ai-skills-collection.git

# 进入技能目录
cd enterprise-ai-skills-collection/skills/ai-driven-economic-research
```

## 技能统计

- **总技能数**: 1
- **已测试技能**: 1
- **平均测试得分**: 89.8/100
- **最后更新**: 2026-05-29

## 贡献指南

欢迎提交新的企业AI技能！请遵循以下规范：

1. 在 `skills/` 目录下创建新技能文件夹
2. 使用 kebab-case 命名（如: `ai-risk-assessment`）
3. 必须包含: SKILL.md, metadata.json, test/test_cases.md
4. 测试得分需达到 80/100 以上
5. 更新 INDEX.md 和 README.md

---

**更新时间**: 2026-05-29
**技能总数**: 1
**维护者**: wanglin1111111
"""
    
    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write(index)
    
    print("  Created: INDEX.md")
    print()

def update_readme():
    """更新README.md修正技能数量"""
    print("[Bonus] Updating README.md...")
    
    readme_path = Path("README.md")
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 修正技能数量
        content = content.replace("**技能总数**: 7+", "**技能总数**: 1")
        content = content.replace("**更新时间**: 2026-05-25", "**更新时间**: 2026-05-29")
        
        # 添加INDEX.md链接
        if "INDEX.md" not in content:
            content = content.replace(
                "---\n\n**更新时间**",
                "## 快速导航\n\n- [技能索引 INDEX.md](INDEX.md) - 查看所有技能\n- [全局元数据 metadata.json](metadata.json) - 机器可读格式\n\n---\n\n**更新时间"
            )
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print("  Updated: README.md")
    else:
        print("  [WARN] README.md not found")
    
    print()

def print_summary():
    """打印修复摘要"""
    print("=" * 50)
    print("Fix completed successfully!")
    print("=" * 50)
    print()
    print("Fixed issues:")
    print("  [✓] 技能文件移动到标准位置 (skills/ai-driven-economic-research/)")
    print("  [✓] 创建根目录 metadata.json")
    print("  [✓] 创建技能级 metadata.json")
    print("  [✓] 创建全局索引 INDEX.md")
    print("  [✓] 修正 README.md 技能数量 (7+ -> 1)")
    print()
    print("New directory structure:")
    print("  enterprise-ai-skills-collection/")
    print("  ├── metadata.json")
    print("  ├── README.md")
    print("  ├── INDEX.md")
    print("  └── skills/")
    print("      └── ai-driven-economic-research/")
    print("          ├── SKILL.md")
    print("          ├── QUICKREF.md")
    print("          ├── metadata.json")
    print("          ├── test/")
    print("          │   └── test_cases.md")
    print("          └── example/")
    print("              └── (empty)")
    print()
    print("Next steps:")
    print("  1. Review the changes")
    print("  2. git add -A")
    print("  3. git commit -m 'fix: 修复P0级问题 - 标准化目录结构'")
    print("  4. git push origin main")
    print