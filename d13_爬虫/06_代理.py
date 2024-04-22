import urllib.request

#url='http://www.baidu.com'
my_url='https://ip.900cha.com'

my_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}
req=urllib.request.Request(url=my_url,headers=my_headers)

proxies={
    'http':'183.240.222.103:40009' #不好用
}

#ProxyHandler
handler=urllib.request.ProxyHandler(proxies=proxies)

opener=urllib.request.build_opener(handler)

response=opener.open(req)

content=response.read().decode('UTF-8')

print(content)

with open('daili.html','w',encoding='UTF-8')as fp:
    fp.write(content)
