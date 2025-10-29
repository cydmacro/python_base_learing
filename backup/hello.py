# 经典入门程序 
print("Hello World!")  # 打印输出
print(2 + 3 * 4)       # 数学运算


# 正确示例
age = 18              # 纯字母
student_name = "冰冰"  # 含下划线 java 里面studentName
_price = 9.9          # 以下划线开头
MAX_COUNT = 100       # 全大写常量（约定俗成）


# 2name = "错误"        # ❌ 数字开头
# class = "计算机"      # ❌ 使用保留字
# first-name = "张"     # ❌ 含连字符

"""
计算圆的面积（解释代码作用）
"""
radius = 5
area = 3.14 * radius ** 2  # 公式 πr²
print("圆的面积是："+ str(area))

"""
作者：学习python-test
日期：2030-10-01
功能：计算BMI指数
参数说明：
  weight: 体重(kg)
  height: 身高(m)

public static String cal(){
    
}
  
"""
def calc_bmi(weight, height):
    print("weight:", weight)
    print("height:", height)
print(1111)
calc_bmi(222,333)

# 查看当前版本关键字
import keyword
print(keyword.kwlist)


if 10>4:
    print("10大于4")
elif 10<4:
    print("10小于4")
    print("aaaa")
else:
    print("10等于4")
    
# 错误示例
#class = "计算机科学"  # ❌ class是关键字

# 正确写法
class_name = "计算机科学"

