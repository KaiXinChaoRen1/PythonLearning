
class student:
    #成员变量(有了构造函数可以省略)

    #成员方法(参数必须要有self)
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self. age=age
        print("student类创建了一个对象")
    
    def talk(self,country):
        print(f"我的名字是{self.name},我今年{self.age}岁,我是{country}人")
#创建对象
my_stu=student("李文强","男","二十四")

#获取对象的值
print(my_stu.name)
#调用方法
my_stu.talk("中国")