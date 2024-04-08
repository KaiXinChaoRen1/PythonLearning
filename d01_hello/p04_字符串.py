#字符串拼接
name="你爸爸"
print("我是"+name)  
#字符串占位符,可以%s表示转换成字符串,%d:整数 %f:浮点数
your_name="我儿子"
print(type(your_name))
num=999
print("你是%s,我是%s,我有%s个儿子"%(your_name,name,num))
#精度问题
f=19.99
print("数字是%f"%f)
#指定精度(不写就是不限制,例如.3f)
print("数字是%4.4f"%f)

#占位符2(不限制数据类型,不做精度控制)
print(f"你是{your_name},我是{name},我有{num}个儿子")

print(f"你是{your_name},我是{name},我有{99*10}个儿子")
