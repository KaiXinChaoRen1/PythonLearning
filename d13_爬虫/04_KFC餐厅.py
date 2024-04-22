import requests
import json

if __name__ == "__main__":
    # 如果在搜索框输入信息，回车后网址没变而页面有变化，说明这是一个ajax请求
    cityName = input('请输入你想爬取的肯德基餐厅关键字: ')
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    pageIndex = '1'
    data = {
        'cname': '',
        'pid': '',
        'keyword': cityName,
        'pageIndex': pageIndex,
        'pageSize': '10'
    }
    # 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'
    }
    try:
        # 以写文件的形式打开一个文件
        loop = True
        # 这个列表/字典用来存放北京市的所有餐厅的名字，或者用一个字典
        data_list = []
   
        while loop:
            response = requests.post(url=url, data=data, headers=headers)
            json_data = response.json()
            # 使用if not x这种写法的前提是：必须清楚x等于None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()时对你的判断没有影响才行
            if not json_data['Table1']:
                break
            num= len(json_data['Table1'])
            
            for i in range(0, num):
                    my_s =json_data['Table1'][i]['storeName']+'---'+json_data['Table1'][i]['addressDetail']
                    data_list.append(my_s)
                    print(my_s)
            pageIndex = str(int(pageIndex) + 1)
            data['pageIndex'] = pageIndex
        print('-----循环结束-----')

        with open('./BeijingKFC.txt', 'a', encoding='utf-8') as fp:
            fp.write(str(data_list))
    except IOError:
        print('写入异常!')
    else:
        print('写入结束!')
        fp.close()
