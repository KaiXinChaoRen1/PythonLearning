
from pyspark import SparkConf, SparkContext
import os
#配置环境变量
os.environ['PYSPARK_PYTHON'] = "/home/adev/PythonLearning/.venv/bin/python"


conf = SparkConf().setMaster("local[*]").setAppName("flatmap_test")
sc = SparkContext(conf=conf)
 
# flatMap解除嵌套
rdd = sc.parallelize(["a-b-c", "e-f-g", "uuu ggg"])
rdd2 = rdd.flatMap(lambda x: x.split("-"))
print(rdd2.collect())


