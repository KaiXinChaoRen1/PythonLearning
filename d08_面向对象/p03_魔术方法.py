# 除了构造方法,类中还提供了一些其他内置方法(魔术方法  前后都有两个下划线的方法)
class student:
    def __eq__(self, other):
        return self.age == other.age

    def __le__(self, other):
        return self.age <= other.age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f"我的名字是{self.name},我今年{self.age}岁"

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print("student类创建了一个对象")

    def talk(self, country):
        print(f"我的名字是{self.name},我今年{self.age}岁,我是{country}人")


# 创建对象
my_stu = student("李文强", "男", 24)

# 创建对象
my_stu2 = student("钢铁侠", "男", 24)

# 对象的字符串方法
print(my_stu)
# 对象比较
print(my_stu == my_stu2)
