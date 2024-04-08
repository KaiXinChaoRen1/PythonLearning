#为什么安装这个的时候不需要设置清华大学那个网址了?
#引入折现图
from pyecharts.charts import Line
#引入标题设置
from pyecharts.options import TitleOpts


line=Line()
#x轴
line.add_xaxis(["2018","2019","2020"])
#y轴
line.add_yaxis("收入",[-1700,-1600,-1500])
line.add_yaxis("卧推重量",[20,40,60,80])

#设置图表全局选项
line.set_global_opts(
    #设置标题
    title_opts=TitleOpts(title="世界经济格局doge",pos_left="center",pos_bottom="1%")
)

#生成图像
print("生成图像")
line.render()