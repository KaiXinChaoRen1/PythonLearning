#解决类型不确定的问题 3.5以后的功能，用于协助提示
#写不写都行，写错也行，一般在看不出类型的时候才写，比如某个函数的返回值

#变量类型注解
#写法1
a:int=1
s:str="hehe"

#写法2
a1 =1       # type:int
s1="haha"   #type:str



#函数的参数和返回值类型注解

#对参数注解
def add(x:int,y:int):
    return x+y

#对返回注解
def add(x:int,y:int)-> int:
    return x+y


#Union  先导包
from typing import Union

#alist: list[Union(int,str,bool)]  = [99, 2, 2, "3", True]

#adict: dict[str,Union[int,str]]={"name":"liwenqiang","age":23}


