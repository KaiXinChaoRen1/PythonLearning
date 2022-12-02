
num=0

def hehe():
    num=100
    print(num)

hehe()
print(f"函数内对全局变量的修改不会影响外边的变量,所以num是{num}")

def hehe2():
    global num
    num=100
    print(num)

hehe2()
print(f"使用global声明全局变量,这样num是{num}")