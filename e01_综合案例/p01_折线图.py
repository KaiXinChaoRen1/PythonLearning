#为什么安装这个的时候不需要设置清华大学那个网址了?
from pyecharts.charts import Line


line=Line()

line.add_xaxis(["美国","中国","日本"])

line.add_yaxis("人口",[3.3,14.1,1.25])
line.add_yaxis("人均gdp",[7,1.2,4])
#生成图像
line.render()