#open默认gbk 中文要指定编码
my_file=open("/home/adev/PythonLearning/hehe.txt","r",encoding="UTF-8")

#print(my_file.read())
print(my_file.read(2))

print('===========')


with open("/home/adev/PythonLearning/hehe.txt","r",encoding="UTF-8") as my_file:
    print(my_file.read())
