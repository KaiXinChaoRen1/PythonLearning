#包=一堆模块+__init__.py
# 添加项目根目录到 Python 路径
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#vscode里不能用,可能是文件配置路径的问题?
import my_package.my_module

res=my_package.my_module.my_fun(2,2)
print(res)
