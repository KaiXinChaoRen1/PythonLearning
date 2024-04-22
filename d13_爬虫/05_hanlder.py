import urllib.request

#url='http://www.baidu.com'
my_url='https://www.baidu.com'

my_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}
req=urllib.request.Request(url=my_url,headers=my_headers)


handler=urllib.request.HTTPHandler()

opener=urllib.request.build_opener(handler)

response=opener.open(req)

content=response.read().decode('UTF-8')
with open('hanlder.html','w',encoding='UTF-8')as fp:
    fp.write(content)

