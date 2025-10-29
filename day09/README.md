# Day 9: 综合项目实战(上)

> **学习时长**: 1天 (6小时)
> **难度**: ★★★★☆
> **目标**: 完成2个完整项目，掌握OOP设计与生产级代码规范

---

## 📚 学习目标

### 核心知识点
- [x] 文本清洗：正则表达式、批量处理
- [x] 数据集准备：分层采样、类别平衡
- [x] OOP设计：类封装、方法链式调用
- [x] 代码规范：日志系统、配置文件、报告生成

### AI场景应用
- 文本清洗 → NLP标注前预处理
- 数据集划分 → CV模型训练数据准备
- 类别平衡 → 解决样本不均衡问题

---

## 🎯 项目清单

### 📦 Project 1: 文本清洗工具

**目录**: `项目1_文本清洗/`

| 版本 | 文件 | 行数 | 难度 | 特点 |
|------|------|------|------|------|
| v1 | **v1_basic.py** | 80行 | ★★☆☆☆ | 基础正则清洗 |
| v2 | **v2_enhanced.py** | 150行 | ★★★☆☆ | 批量处理+统计 |
| v3 | **v3_complete.py** | 250行 | ★★★★☆ | OOP封装+日志系统 |

**核心功能**：
- 去除特殊字符(emoji、标点、空白)
- 繁简体转换
- 批量文件处理
- 处理统计报告

**运行示例**：
```bash
cd 项目1_文本清洗/

# v1 - 基础版
python v1_basic.py

# v2 - 批量处理版
python v2_enhanced.py

# v3 - 完整OOP版
python v3_complete.py
```

**核心代码片段**：
```python
# v3_complete.py - OOP设计
class TextCleaner:
    def __init__(self, config_file=None):
        self.config = self.load_config(config_file)
        self.stats = {'total': 0, 'cleaned': 0}
        self.setup_logging()

    def clean_text(self, text):
        # 去除emoji
        text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s，。！？]', '', text)
        # 去除多余空白
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def clean_file(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        cleaned = self.clean_text(content)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned)

        self.stats['total'] += 1
        self.stats['cleaned'] += 1
        self.logger.info(f"已清洗: {input_file}")
```

**AI应用场景**：
- NLP标注前的文本预处理
- 去除噪声数据提高标注质量
- 批量清洗大规模语料库

---

### 📦 Project 2: 图片分类数据集准备

**目录**: `项目2_图片分类/`

| 版本 | 文件 | 行数 | 难度 | 特点 |
|------|------|------|------|------|
| v1 | **v1_basic.py** | 100行 | ★★☆☆☆ | 简单80/20划分 |
| v2 | **v2_enhanced.py** | 180行 | ★★★☆☆ | 分层采样+平衡检查 |
| v3 | **v3_complete.py** | 280行 | ★★★★★ | 多种划分策略+完整报告 |

**核心功能**：
- 训练集/测试集/验证集划分
- 分层采样(保持类别比例)
- 类别平衡度检查
- 数据集构建报告

**运行示例**：
```bash
cd 项目2_图片分类/

# v1 - 基础划分
python v1_basic.py

# v2 - 分层采样
python v2_enhanced.py

# v3 - 完整构建器
python v3_complete.py
```

**核心代码片段**：
```python
# v3_complete.py - 数据集构建器
class DatasetBuilder:
    def __init__(self, images, categories=None):
        self.images = images
        self.categories = categories or self.extract_categories()
        self.train_set = []
        self.test_set = []
        self.val_set = []

    def stratified_split(self, train_ratio=0.8, val_ratio=0.0):
        """分层采样划分"""
        # 按类别分组
        cat_groups = {}
        for img in self.images:
            cat = img.split('_')[0]
            cat_groups.setdefault(cat, []).append(img)

        # 对每个类别划分
        for cat, imgs in cat_groups.items():
            random.shuffle(imgs)

            train_point = int(len(imgs) * train_ratio)
            val_point = train_point + int(len(imgs) * val_ratio)

            self.train_set.extend(imgs[:train_point])
            if val_ratio > 0:
                self.val_set.extend(imgs[train_point:val_point])
                self.test_set.extend(imgs[val_point:])
            else:
                self.test_set.extend(imgs[train_point:])

        return self

    def check_balance(self, dataset):
        """检查类别平衡度"""
        counts = {}
        for img in dataset:
            cat = img.split('_')[0]
            counts[cat] = counts.get(cat, 0) + 1

        max_count = max(counts.values())
        min_count = min(counts.values())
        return (min_count / max_count) * 100
```

**AI应用场景**：
- CV模型训练数据集准备
- 确保各类别样本均衡
- 避免模型偏向某一类别

---

## 📂 测评答案 (2个)

| 文件 | 说明 |
|------|------|
| **Day9_测评_实操题1_文本清洗_v1.py** | 文本清洗综合练习 |
| **Day9_测评_实操题2_图片数据集准备_v1.py** | 数据集划分综合练习 |

**测评题目**：查看 [`../../测评/Day9_测评.md`](../../测评/Day9_测评.md)

---

## 📖 配套教案

- **教案位置**: [`../../教案/第九章.md`](../../教案/第九章.md)
- **章节标题**: 综合项目实战(上)
- **内容范围**: 第九章全部内容

---

## 🎯 学习路径建议

### 项目1学习路径 (3小时)
1. **v1_basic.py** (30分钟)
   - 理解正则表达式基础
   - 掌握文本清洗核心逻辑
   - 运行测试基础功能

2. **v2_enhanced.py** (1小时)
   - 学习批量文件处理
   - 理解统计信息收集
   - 练习函数封装

3. **v3_complete.py** (1.5小时)
   - 掌握OOP类设计
   - 学习日志系统配置
   - 理解配置文件分离

### 项目2学习路径 (3小时)
1. **v1_basic.py** (30分钟)
   - 理解数据集划分原理
   - 掌握简单随机划分
   - 计算数据集统计

2. **v2_enhanced.py** (1小时)
   - 学习分层采样算法
   - 实现类别平衡检查
   - 生成分布统计报告

3. **v3_complete.py** (1.5小时)
   - 掌握DatasetBuilder设计模式
   - 学习多种划分策略
   - 理解完整报告生成

---

## 💡 项目版本对比

### 文本清洗工具版本对比

| 特性 | v1_basic | v2_enhanced | v3_complete |
|------|----------|-------------|-------------|
| **基础清洗** | ✅ | ✅ | ✅ |
| **批量处理** | ❌ | ✅ | ✅ |
| **统计功能** | ❌ | ✅ | ✅ |
| **OOP设计** | ❌ | ❌ | ✅ |
| **日志系统** | ❌ | ❌ | ✅ |
| **配置文件** | ❌ | ❌ | ✅ |
| **代码量** | 80行 | 150行 | 250行 |

### 数据集准备工具版本对比

| 特性 | v1_basic | v2_enhanced | v3_complete |
|------|----------|-------------|-------------|
| **简单划分** | ✅ | ✅ | ✅ |
| **分层采样** | ❌ | ✅ | ✅ |
| **平衡检查** | ❌ | ✅ | ✅ |
| **验证集** | ❌ | ❌ | ✅ |
| **OOP设计** | ❌ | ❌ | ✅ |
| **完整报告** | ❌ | ❌ | ✅ |
| **JSON导出** | ❌ | ❌ | ✅ |
| **代码量** | 100行 | 180行 | 280行 |

---

## 🔍 常见问题

### Q1: 为什么需要分层采样？
**A**: 保持训练集和测试集的类别比例一致，避免划分偏差导致模型评估不准确。

### Q2: 类别平衡度多少算合格？
**A**: 一般要求 ≥70%，即最少类别样本数 ≥ 最多类别样本数的70%。

### Q3: 什么时候需要验证集？
**A**: 调参时需要。训练集训练模型，验证集调超参数，测试集最终评估。

### Q4: v3的OOP设计有什么好处？
**A**:
- 代码复用性高
- 易于扩展新功能
- 符合生产级代码规范
- 方便团队协作维护

---

## 📊 本日项目统计

| 项目 | 版本数 | 总代码量 | 平均行数 |
|------|--------|----------|----------|
| 文本清洗 | 3个 | 480行 | 160行/版本 |
| 图片分类 | 3个 | 560行 | 187行/版本 |
| 测评答案 | 2个 | 300行 | 150行/文件 |
| **Day9总计** | **8个** | **~1340行** | **168行/文件** |

---

## 🎓 毕业要求

完成Day9学习后，应达到以下水平：

- ✅ 能独立完成v2级别项目(150-180行)
- ✅ 理解v3级别的OOP设计思想
- ✅ 掌握正则表达式实际应用
- ✅ 理解分层采样原理
- ✅ 能将项目应用到AI标注实际工作

---

## 🔗 相关链接

- [上一章: Day 8 - AI标注工具实战](../day08/README.md) | [下一章: Day 10 - 综合项目实战(下)](../day10/README.md)
- [返回总目录](../README.md)
- [查看教案](../../教案/第九章.md)
- [查看测评](../../测评/Day9_测评.md)
- [原项目参考](../../项目案例/)

---

**最后更新**: 2025-10-29
**完成情况**: ✅ 所有项目代码已创建
**测试状态**: ✅ v1/v2/v3版本全部可运行
