# 第十章:项目实战(二)与毕业设计

> **最终挑战** - 综合大项目,展示学习成果
> **学习目标**: 完成毕业项目,建立职业自信
> **课程时长**: 全天6小时(项目+答辩)

---

## 项目3: AI训练数据CSV处理工具

### 项目背景
公司每天收到大量CSV格式的标注数据,需要自动化处理工具提升效率。

### 功能要求
1. **数据读取**: 支持批量读取多个CSV文件
2. **数据清洗**: 自动去除缺失/重复/异常数据
3. **数据统计**: 生成质量报告
4. **数据导出**: 保存为标准格式

### 完整代码
```python
import pandas as pd
import os
from datetime import datetime

class DataProcessor:
    """AI训练数据处理工具"""

    def __init__(self):
        self.data = None

    def load_csv(self, file_path):
        """读取CSV文件"""
        self.data = pd.read_csv(file_path, encoding='utf-8')
        print(f"✅ 已读取: {file_path}, {len(self.data)}条数据")

    def clean_data(self):
        """数据清洗"""
        original_count = len(self.data)

        # 删除缺失值
        self.data = self.data.dropna()

        # 删除重复值
        self.data = self.data.drop_duplicates()

        cleaned_count = len(self.data)
        print(f"✅ 清洗完成: {original_count} → {cleaned_count}条")

    def generate_report(self):
        """生成质量报告"""
        report = f"""
===== 数据质量报告 =====
生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
总样本数: {len(self.data)}
总字段数: {len(self.data.columns)}

字段列表: {', '.join(self.data.columns)}

数据预览:
{self.data.head()}

统计摘要:
{self.data.describe(include='all')}
        """
        print(report)
        return report

    def export(self, output_path):
        """导出数据"""
        self.data.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"✅ 已保存到: {output_path}")

# 使用示例
processor = DataProcessor()
processor.load_csv('raw_data.csv')
processor.clean_data()
processor.generate_report()
processor.export('clean_data.csv')
```

### 技能点
- 面向对象编程(类和方法)
- 完整工具封装
- 自动化流程

---

## 毕业项目答辩

### 答辩要求
1. **演示项目**: 现场运行代码,展示效果
2. **讲解思路**: 说明如何解决问题
3. **代码说明**: 解释关键代码逻辑
4. **回答问题**: 应对老师提问

### 评分标准
| 评分项 | 权重 | 说明 |
|--------|------|------|
| 功能完整性 | 40% | 实现全部要求功能 |
| 代码质量 | 30% | 逻辑清晰,注释完整 |
| 演示效果 | 20% | 流畅演示,无错误 |
| 问题回答 | 10% | 理解原理,思路清晰 |

### 优秀案例特征
✅ 代码运行无错误
✅ 功能超出基本要求
✅ 添加个人创新点
✅ 讲解清晰有条理

---

## 学习成果总结

### 10天学习路线图
```
Day 1-2: Python基础语法
Day 3-4: 数据结构与流程控制
Day 5-6: 函数与OOP
Day 7: Pandas数据处理
Day 8: AI标注实战
Day 9: 项目实战(文本+图片)
Day 10: 综合项目+答辩
```

### 掌握的技能清单
✅ Python核心语法
✅ 数据处理(Pandas)
✅ 文件操作
✅ 数据清洗
✅ 项目开发流程
✅ AI标注工具使用

### 职业发展路径

**Level 1: 数据标注员**(1-2周达到)
- 工作内容: 标注数据
- 月薪范围: 4000-6000元

**Level 2: 质检员**(1-2月达到)
- 工作内容: 质量检查
- 月薪范围: 6000-8000元

**Level 3: 数据处理工程师**(3-6月达到)
- 工作内容: 数据清洗,工具开发
- 月薪范围: 8000-12000元

**Level 4: AI训练师**(6-12月达到)
- 工作内容: 标注规范制定,模型训练支持
- 月薪范围: 12000-20000元

---

## 结业寄语

恭喜你完成Python基础教学全部课程!🎉

10天时间,从零基础到能独立完成AI数据处理项目,这是巨大的进步!

**下一步建议**:
1. 持续练习,巩固技能
2. 关注AI行业动态
3. 积累项目经验
4. 考虑进阶学习(深度学习/算法)

**记住**: 学习永无止境,保持好奇心和学习热情!

祝你在AI领域发展顺利!💪
