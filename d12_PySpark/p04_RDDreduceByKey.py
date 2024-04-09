from pyspark import SparkConf, SparkContext
import os
#配置环境变量
os.environ['PYSPARK_PYTHON'] = "/home/adev/PythonLearning/.venv/bin/python"

conf = SparkConf().setMaster("local[*]").setAppName("reduceByKey_test")
sc = SparkContext(conf=conf)
 
# 准备一个RDD
rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 99), ('女', 66)])
# 求男生和呃女生两个组的成绩之和
rdd1 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd1.collect())