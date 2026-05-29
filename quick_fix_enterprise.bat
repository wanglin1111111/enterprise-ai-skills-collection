@echo off
chcp 65001
cls
echo ==========================================
echo Enterprise AI Skills Collection - Quick Fix
echo ==========================================
echo.

REM 创建标准目录结构
echo [1/4] Creating standard directory structure...
if not exist "skills" mkdir skills
if not exist "skills\ai-driven-economic-research" mkdir skills\ai-driven-economic-research
if not exist "skills\ai-driven-economic-research\test" mkdir skills\ai-driven-economic-research\test
if not exist "skills\ai-driven-economic-research\example" mkdir skills\ai-driven-economic-research\example
echo     Created: skills/ai-driven-economic-research/
echo.

REM 移动技能文件到标准位置
echo [2/4] Moving skill files to standard location...
if exist "SKILL.md" (
    move /Y "SKILL.md" "skills\ai-driven-economic-research\SKILL.md" >nul
    echo     Moved: SKILL.md -> skills/ai-driven-economic-research/
)
if exist "QUICKREF.md" (
    move /Y "QUICKREF.md" "skills\ai-driven-economic-research\QUICKREF.md" >nul
    echo     Moved: QUICKREF.md -> skills/ai-driven-economic-research/
)
if exist "TEST.md" (
    move /Y "TEST.md" "skills\ai-driven-economic-research\test\test_cases.md" >nul
    echo     Moved: TEST.md -> skills/ai-driven-economic-research/test/
)
echo.

REM 创建metadata.json
echo [3/4] Creating metadata.json...
(
echo {
echo   "name": "ai-driven-economic-research",
echo   "version": "1.0.0",
echo   "description": "AI技术在经济学研究中的系统化应用框架，涵盖非传统数据处理、预测分析方法、跨学科融合研究、就业影响评估四大核心模块",
echo   "category": "research",
echo   "author": "wanglin1111111",
echo   "license": "MIT",
echo   "keywords": [
echo     "economics",
echo     "ai-research",
echo     "text-analysis",
echo     "image-analysis",
echo     "forecasting",
echo     "policy-analysis",
echo     "employment-impact"
echo   ],
echo   "test_score": 89.8,
echo   "test_grade": "A",
echo   "created_at": "2026-05-25",
echo   "updated_at": "2026-05-29",
echo   "files": {
echo     "skill": "skills/ai-driven-economic-research/SKILL.md",
echo     "quickref": "skills/ai-driven-economic-research/QUICKREF.md",
echo     "test": "skills/ai-driven-economic-research/test/test_cases.md"
echo   }
echo }
) > metadata.json
echo     Created: metadata.json
echo.

REM 创建全局索引
echo [4/4] Creating global index...
(
echo # Enterprise AI Skills Collection
echo.
echo ^> 企业AI应用技能集合 - 统一仓库
echo.
echo ## 技能列表
echo.
echo | 技能名称 | 描述 | 测试得分 | 状态 |
echo |----------|------|----------|------|
echo | [AI驱动的经济学研究](skills/ai-driven-economic-research/) | AI技术在经济学研究中的系统化应用框架 | 89.8/100 (A) | ✅ 可用 |
echo.
echo ## 技能详情
echo.
echo ### AI驱动的经济学研究 (ai-driven-economic-research)
echo.
echo - **描述**: AI技术在经济学研究中的系统化应用框架
echo - **核心内容**: 文本数据分析、图像数据应用、预测方法融合、就业影响评估
echo - **测试得分**: 89.8/100 (A)
echo - **文件位置**: [skills/ai-driven-economic-research/](skills/ai-driven-economic-research/)
echo - **适用人群**: 经济研究人员、数据科学家、政策分析师、社会科学研究者
echo.
echo #### 核心模块
echo.
echo 1. **文本数据量化分析**
echo    - 主题提取、情感分析、文本分类
echo    - 政府报告、会议纪要、历史文献分析
echo.
echo 2. **图像数据应用**
echo    - 卫星图像、街景图像、医疗影像分析
echo    - 物体识别、场景分析、变化检测
echo.
echo 3. **预测方法融合**
echo    - 经济指标预测、市场趋势分析
echo    - 机器学习预测模型、因果推断
echo.
echo 4. **就业影响评估**
echo    - 就业结构分析、收入分配研究
echo    - AI对劳动力市场的影响评估
echo.
echo ## 目录结构
echo.
echo ```
echo enterprise-ai-skills-collection/
echo ├── metadata.json                    # 全局元数据
echo ├── README.md                        # 项目说明
echo ├── INDEX.md                         # 技能索引（本文件）
echo └── skills/
echo     └── ai-driven-economic-research/   # 技能目录
echo         ├── SKILL.md                   # 技能文档
echo         ├── QUICKREF.md                # 快速参考
echo         ├── metadata.json              # 技能元数据
echo         ├── test/
echo         │   └── test_cases.md          # 测试用例
echo         └── example/
echo             └── real_world_examples.md # 使用示例
echo ```
echo.
echo ## 使用方式
echo.
echo ### 查看技能详情
echo.
echo ```bash
echo # 阅读完整技能文档
cat skills/ai-driven-economic-research/SKILL.md
echo.
echo # 查看快速参考
cat skills/ai-driven-economic-research/QUICKREF.md
echo.
echo # 查看测试用例
cat skills/ai-driven-economic-research/test/test_cases.md
echo ```
echo.
echo ### 安装技能
echo.
echo ```bash
echo # 克隆仓库
git clone https://github.com/wanglin1111111/enterprise-ai-skills-collection.git
echo.
echo # 进入技能目录
cd enterprise-ai-skills-collection/skills/ai-driven-economic-research
echo ```
echo.
echo ## 技能统计
echo.
echo - **总技能数**: 1
echo - **已测试技能**: 1
echo - **平均测试得分**: 89.8/100
echo - **最后更新**: 2026-05-29
echo.
echo ## 贡献指南
echo.
echo 欢迎提交新的企业AI技能！请遵循以下规范：
echo.
echo 1. 在 `skills/` 目录下创建新技能文件夹
echo 2. 使用 kebab-case 命名（如: `ai-risk-assessment`）
echo 3. 必须包含: SKILL.md, metadata.json, test/test_cases.md
echo 4. 测试得分需达到 80/100 以上
echo 5. 更新 INDEX.md 和 README.md
echo.
echo ---
echo.
echo **更新时间**: 2026-05-29
echo **技能总数**: 1
echo **维护者**: wanglin1111111
echo.
) > INDEX.md
echo     Created: INDEX.md
echo.

REM 创建技能级metadata.json
echo [Bonus] Creating skill-level metadata.json...
(
echo {
echo   "name": "ai-driven-economic-research",
echo   "version": "1.0.0",
echo   "description": "AI技术在经济学研究中的系统化应用框架",
echo   "category": "research",
echo   "author": "wanglin1111111",
echo   "license": "MIT",
echo   "keywords": [
echo     "economics",
echo     "ai-research",
echo     "text-analysis",
echo     "image-analysis",
echo     "forecasting"
echo   ],
echo   "test_score": 89.8,
echo   "test_grade": "A",
echo   "created_at": "2026-05-25",
echo   "updated_at": "2026-05-29",
echo   "files": [
echo     "SKILL.md",
echo     "QUICKREF.md",
echo     "test/test_cases.md"
echo   ]
echo }
) > skills\ai-driven-economic-research\metadata.json
echo     Created: skills/ai-driven-economic-research/metadata.json
echo.

echo ==========================================
echo Fix completed successfully!
echo ==========================================
echo.
echo Fixed issues:
echo   [✓] 技能文件移动到标准位置
echo   [✓] 创建 metadata.json
echo   [✓] 创建全局索引 INDEX.md
echo   [✓] 修正技能数量声明 (7+ -> 1)
echo.
echo Next steps:
echo   1. Review the changes
echo   2. Update README.md skill count
echo   3. Commit and push
echo.
pause
