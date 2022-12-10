#json是自带模块
import json  
my_data=[{"name":"李文强","age":"23"},{"name":"李文强2","age":"24"},{"name":"李文强3","age":"25"}]
json_str=json.dumps(my_data,ensure_ascii=False) #ensure_ascii=False中文
print(json_str)


res=json.loads(json_str)
print(type(res))
print(res)