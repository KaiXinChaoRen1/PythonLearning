# 五类 列表:list
# 元组:tuple 字符串:str  集合:set 字典:dict

# 数据上限为 2**63-1(非常非常大)
# 列表内元素可以不是统一类型
# 定义列表
list0 = [99, 2, 2, "3", True]
# 定义空列表
list1 = []
list2=list()

print(list)
print(list1)
print(list2)
# 取出列表元素
print(list[3])

# class的成员函数成为方法,需要使用class.方法调用
# index()获取元素在list中的下标(这里True会转成1)
index = list0.index(2)
print(f"index()获取的下标是{index}")
# 插入元素
list0.insert(0, 999)
print(list0)
# 追加元素到尾部
list0.append(False)
print(list0)
# 追加其他数据容器
set = set([1, 1, 2, 2, 3, 3])
list0.extend(set)
print(list0)

# 删除指定位置元素del直接删除,pop是删除并返回,remove是删除指定元素在集合中的第一个,clear清空
pop = list0.pop(0)
print(f"pop出来的元素是{pop},剩下的集合是{list0}")
# count()统计某个元素数量
count = list0.count(2)
len = len(list0)
print(f"指定元素的数量是{count},所有元素的数量是{len}")
