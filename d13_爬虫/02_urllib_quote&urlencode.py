#urllib.parse.quote URL编码的方式是把需要编码的字符转化为 %xx 的形式
import urllib.request
import urllib.parse


my_url='https://www.baidu.com/s?wd='

data={
    'wd':'林俊杰'
    #'sex':'男'
}

my_data=urllib.parse.urlencode(data)



name=urllib.parse.quote('林俊杰')

my_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}



print(my_url+my_data)
print(my_url+name)