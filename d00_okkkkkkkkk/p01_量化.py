#pip install pandas yfinance matplotlib
import yfinance as yf


# 指定股票代码
name = 'AAPL'

# 下载历史价格数据
apple = yf.download(name, start='2022-01-01', end='2022-12-31')
print(apple.head())