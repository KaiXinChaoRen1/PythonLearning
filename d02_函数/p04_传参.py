"""
演示多种传参的形式
"""


def user_info(name, age, gender):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")


# 按照位置
user_info('小明', 20, '男')

# 关键字参数
user_info(name='冰冰', age=18, gender='女')
user_info(age=17, gender='女', name='潇潇')    # 可以不按照参数的定义顺序传参
user_info('甜甜', gender='女', age=19)


# 缺省参数（默认值）需要放在最后面
def user_info(name, age, gender,country="中国"):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender},国家是:{country}")
user_info('小天', 13, '男')
user_info('布鲁斯', 13, '男',"外国")


# 不定长 - 位置不定长, *号
# 不定长定义的形式参数会作为元组
def user_info(*args):
    print(f"args参数的类型是：{type(args)}，内容是:{args}")
user_info(1, 2, 3, '小明', '男孩')


# 不定长 - 关键字不定长, **号
## 不定长定义的形式参数会作为字典
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)}，内容是:{kwargs}")
user_info(name='小王', age=11, gender='男孩')
