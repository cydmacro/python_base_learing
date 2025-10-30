"""
Day 3 测评 - 实操题1: 学生信息管理(字典)
解法1: 基础版
"""

# 创建学生信息字典
student = {'姓名': '张三', '年龄': 20, '成绩': 85}

# 添加班级字段
student['班级'] = 'Python基础班'

# 修改成绩
student['成绩'] = 90

# 打印所有键值对
print("=" * 50)
print("学生信息管理系统")
print("=" * 50)
for key, value in student.items():
    print(f"{key}: {value}")
print("=" * 50)
