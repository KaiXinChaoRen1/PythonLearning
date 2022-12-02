def my_len(data):
    count=0
    for i in data:
        count+=1
    print(f"输入的长度为{count}")

my_len("我是你爸爸")
#参数乱输报错
#my_len(10)

#******************************************
def add(x,y):
    print(f"{x}+{y}的值是{x+y}")
    return x+y

add(3,2)
add(3.1,3.8)
add("hehe","haha")

res=add(9,9)
print(res)

#***************************************
#无返回值函数,其实返回的是None
#None在if中相当于False
variable=my_len("hehe")
print(variable)
print(f"{variable}的类型是{type(variable)}")