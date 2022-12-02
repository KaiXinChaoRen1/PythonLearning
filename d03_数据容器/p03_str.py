#字符串也是无法修改的,修改只会得到一个新的字符串

str1="我,是,你,爸,爸"
print(str1.index("爸,爸"))

#会生成一个新的字符串
print(str1.replace("爸,爸","爷,爷"))

liststr=str1.split(",")
print(f"分割后的结果是{liststr},他的类型是{type(liststr)}")

#strip不传参数,取出前后空格和回车,加参数,取出前后其参数的字串
str2="  我是你爸爸  "
print(str2)
print(str2.strip())
str3="12我是你爸爸21"
print(str3.strip("21"))
#count()  len()