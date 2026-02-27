from pathlib import Path


print("我是你爸爸")#这是注释？
# codespace 666!!!
print("111打印__name__是:"+__name__)

# codespace 666!!!
print("222打印__file__是:"+__file__)

#输出__file__的绝对路径
print("333打印__file__是:" + str(Path(__file__).resolve()))

#输出Path(__file__).resolve()的对象类型
print("444type(Path(__file__).resolve())是:",type(Path(__file__).resolve()))




