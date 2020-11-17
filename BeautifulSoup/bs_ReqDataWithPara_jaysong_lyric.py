# 直接运行代码就好
import requests
# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
for x in range(1):
    params = {
    'ct': '24',
    'qqmusic_ver': '1298',
    'remoteplace': 'txt.yqq.lyric',
    'searchid': '102722342034303519',
    'aggr': '0',
    'catZhida': '1',
    'lossless': '0',
    'sem': '1',
    't': '7',
    'p': 'str(i+1)',
    'n': '5',
    'w': '周杰伦',
    'g_tk_new_20200303': '5381',
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0'  
    }
    # 将参数封装为字典
    res_lyric = requests.get(url,headers=headers,params=params)
    # 调用get方法，下载这个字典
    json_lyric = res_lyric.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_lyric = json_lyric['data']['lyric']['list']
    # 一层一层地取字典，获取歌词列表
    for lyrics in list_lyric:
    # list_lyric是一个列表，lyrics是它里面的元素
        print(lyrics['content'].replace('\\n','\n'))
        print('________________________________________________________')
