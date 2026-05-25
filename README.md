# AI-Driven Economic Research

> AI驱动的经济学研究方法论 - 非传统数据处理、预测分析、跨学科融合、就业影响评估

## 📖 技能简介

本技能提供AI技术在经济学研究中的系统化应用框架，涵盖文本数据分析、图像数据应用、预测方法融合、就业影响评估四大核心模块。适用于经济研究人员、数据科学家、政策分析师、社会科学研究者。

## 🎯 核心能力

### 1. 文本数据量化分析
- 政策文本主题提取与情感分析
- 历史文献量化研究（如古代幸福指数）
- 会议纪要分析（如美联储发言不确定性指数）

### 2. 图像数据经济应用
- 卫星图像经济评估（建筑物、道路、车辆识别）
- 街景图像城市规划（绿化、涂鸦、行人分析）
- 夜间灯光数据区域发展监测

### 3. 预测与因果推断融合
- 双模型法（ML预测 + 计量解释）
- 特征工程辅助（ML特征 + 计量建模）
- 因果机器学习（Causal Forest、Double ML）

### 4. 就业结构影响评估
- 岗位替代风险预测
- 新岗位创造分析
- 政策应对建议（教育、社会保障、产业政策）

## 📚 技能文件

- **SKILL.md** - 核心方法论与框架（完整版）
- **QUICKREF.md** - 快速参考卡片（速查版）
- **TEST.md** - 测试案例集（验证版）

## 🚀 快速开始

### 场景1：政策文本分析
```python
# 步骤1：数据准备
texts = load_policy_reports("2020-2026")

# 步骤2：特征提取
topics = extract_topics(texts, method="BERTopic")
sentiments = analyze_sentiment(texts, method="VADER")

# 步骤3：计量分析
correlation = correlate(sentiments, market_volatility)
```

### 场景2：卫星图像评估
```python
# 步骤1：图像采集
images = download_satellite_images("长三角", "2015-2025")

# 步骤2：特征提取
buildings = detect_objects(images, model="YOLO", target="building")
roads = detect_objects(images, model="YOLO", target="road")

# 步骤3：经济建模
gdp_estimate = build_model(buildings, roads, vehicles)
```

### 场景3：就业影响评估
```python
# 步骤1：岗位分类
jobs = classify_jobs_by_risk(job_data, automation_level)

# 步骤2：预测模型
displacement = predict_displacement(jobs, tech_progress)
creation = predict_creation(jobs, new_industries)

# 步骤3：政策建议
policy = generate_policy(displacement, creation)
```

## 🔗 与其他技能协同

- **macro-micro-linkage-analysis** - 提供宏观-中观-微观三层联动框架
- **quant-invest-analysis** - 提供量化投资分析方法
- **safe-decision-framework** - 提供安全决策原则
- **agent-native-programming** - 提供Agent开发方法论

## 📊 应用案例

| 案例 | 数据源 | 方法 | 应用 |
|------|--------|------|------|
| 美联储政策不确定性指数 | 会议纪要 | NLP + 计量 | 预测市场波动 |
| 中国古代经济史研究 | 历史文献 | 文本情感分析 | 古代幸福指数 |
| 长三角经济监测 | 卫星图像 | CV + 经济建模 | 区域GDP估计 |
| 制造业就业预测 | 岗位数据 | 替代模型 + 情景分析 | 教育政策建议 |

## 🛡️ 核心原则

1. **方法论融合** - AI补充而非替代传统计量经济学
2. **数据驱动** - 非传统数据与传统数据结合
3. **预测与因果并重** - 追求准确性不放弃解释性
4. **伦理优先** - 数据隐私、算法偏见、政策影响评估
5. **跨学科协作** - 经济学 + 计算机科学 + 统计学 + 领域专家

## 📝 引用

如果您在研究中使用本技能，请引用：

```bibtex
@misc{ai-economic-research-2026,
  author = {AutoClaw},
  title = {AI-Driven Economic Research: Methodology and Applications},
  year = {2026},
  url = {https://github.com/wanglin1111111/ai-driven-economic-research}
}
```

## 📜 许可证

MIT License

---

**核心认知**：AI正在深刻改变经济学研究的方法和视角，从数据处理到预测分析，从跨学科融合到社会政策创新。经济学研究的未来是AI与人类智能的深度融合。
