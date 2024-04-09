
from pyspark import SparkConf, SparkContext
 
# 创建sparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext对象,是pyspark操作的唯一入口
sc = SparkContext(conf=conf)


# 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
# 查看rdd里面的内容需要使用collect()方法
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

#加载文件
rdd6 = sc.textFile("/home/adev/PythonLearning/render.html")
print(rdd6.collect())


# 打印PySpark的运行版本
print(sc.version)
# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()

