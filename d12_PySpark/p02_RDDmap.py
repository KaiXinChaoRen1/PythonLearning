from pyspark import SparkConf, SparkContext
import os
#配置环境变量
os.environ['PYSPARK_PYTHON'] = "/home/adev/PythonLearning/.venv/bin/python"
 
conf = SparkConf().setMaster("local[*]").setAppName("map_test")
sc = SparkContext(conf=conf)
 
# 准备RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
 
 
# 通过map方法将全部数据都乘以10
# (T) -> U
def func(data):
    return data * 10
 
 
rdd2 = rdd.map(func)
print(rdd2.collect())
 
# 链式调用,快速解决
rdd3 = rdd.map(lambda e: e * 100).map(lambda e: e + 6)
print(rdd3.collect())
