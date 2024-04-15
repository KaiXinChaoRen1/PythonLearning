import urllib.request

#url='http://www.baidu.com'
my_url='https://www.baidu.com'

my_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}
req=urllib.request.Request(url=my_url,headers=my_headers)


response = urllib.request.urlopen(req)


print(response.read().decode('utf-8'))
print(f"response的类型是{type(response)}") 

