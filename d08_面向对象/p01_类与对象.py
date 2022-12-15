#创建类
class student:
    #成员变量
    name=None
    gender=None
    age=None
    #成员方法(参数必须要有self)
    def talk(self,country):
        print(f"我的名字是{self.name},我今年{self.age}岁,我是{country}人")
#创建对象
my_stu=student()
#对象赋值
my_stu.name="李文强"
my_stu.gender="男"
my_stu.age="二十三"
#获取对象的值
print(my_stu.name)
#调用方法
my_stu.talk("中国")
