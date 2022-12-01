
import time
a=0
while(a<5):
    time.sleep(0.5)
    print(f"hehe{a}")
    a+=1



#for循环中in后面的被称之为序列类型,是指其内容可以被一个个取出的一种类型
str="我是你爸爸"
for i in str:   
    print(i)

#reange()获取一个数字序列--两个参数代表从第一个到第二个(不含第二个),三个参数代表第一个到第二个,步长是第三个
for i in range(5):
    print(i)
    print("hehe")
#此处不再循环里了,说明是通过缩进控制范围的
print("哈哈")