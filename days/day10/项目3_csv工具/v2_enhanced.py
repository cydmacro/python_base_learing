"""
Project 3: CSV数据处理工具
版本: v2 - 改进版 (220行)
功能: 函数模块化 + 多种筛选条件
难度: ★★★☆☆
"""

import csv

def load_csv(file_path):
    """加载CSV文件"""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_csv(data, file_path):
    """保存CSV文件"""
    if not data:
        return False

    with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return True

def clean_data(data):
    """数据清洗"""
    # 去除缺失值
    before = len(data)
    data = [row for row in data if all(row.values())]
    print(f"  删除缺失值: {before - len(data)}条")

    # 去除重复
    before = len(data)
    seen = set()
    unique_data = []
    for row in data:
        row_tuple = tuple(row.items())
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_data.append(row)
    print(f"  去除重复: {before - len(unique_data)}条")

    return unique_data

def filter_data(data, conditions):
    """数据筛选"""
    filtered = []
    for row in data:
        match = True
        for key, value in conditions.items():
            if key not in row or str(row[key]) != str(value):
                match = False
                break
        if match:
            filtered.append(row)

    return filtered

def filter_by_range(data, field, min_val, max_val):
    """范围筛选"""
    filtered = []
    for row in data:
        try:
            val = int(row.get(field, 0))
            if min_val <= val <= max_val:
                filtered.append(row)
        except ValueError:
            continue
    return filtered

# 主程序
print("=" * 70)
print("CSV数据处理工具 v2.0 - 多功能版")
print("=" * 70)

# 创建测试数据
test_data = """name,age,score,city
张三,20,85,北京
李四,22,92,上海
王五,21,78,北京
赵六,20,88,上海
张三,20,85,北京
钱七,,88,广州
孙八,23,95,北京
"""

with open('students.csv', 'w', encoding='utf-8-sig') as f:
    f.write(test_data)

# 加载数据
print("\n1. 加载数据")
data = load_csv('students.csv')
print(f"   读取到 {len(data)} 条数据")

# 清洗数据
print("\n2. 清洗数据")
data = clean_data(data)
print(f"   清洗后剩余 {len(data)} 条数据")

# 条件筛选
print("\n3. 条件筛选")
beijing_students = filter_data(data, {'city': '北京'})
print(f"   北京的学生: {len(beijing_students)}人")

# 范围筛选
print("\n4. 范围筛选")
high_score = filter_by_range(data, 'score', 85, 100)
print(f"   成绩85-100的学生: {len(high_score)}人")

# 保存结果
print("\n5. 保存结果")
save_csv(data, 'students_cleaned.csv')
save_csv(beijing_students, 'students_beijing.csv')
save_csv(high_score, 'students_high_score.csv')

print("\n✓ 处理完成!")
print("  - students_cleaned.csv (清洗后数据)")
print("  - students_beijing.csv (北京学生)")
print("  - students_high_score.csv (高分学生)")
