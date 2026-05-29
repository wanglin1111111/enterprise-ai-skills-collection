# Enterprise AI Skills Collection

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
