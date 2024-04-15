import urllib.request
import urllib.parse
import json

my_url='https://fanyi.baidu.com/sug'

my_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

date={
    'kw':'中国'
}

#post 请求参数必须编码
my_data=urllib.parse.urlencode(date).encode('utf-8')

req=urllib.request.Request(url=my_url,headers=my_headers,data=my_data)

response = urllib.request.urlopen(req)

content= response.read().decode('utf-8')
json=json.loads(content)

print(content)
print(json)
