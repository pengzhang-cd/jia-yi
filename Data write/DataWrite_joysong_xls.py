# 直接运行代码就好
# 引用requests模块
import requests
import openpyxl 
wb = openpyxl.Workbook() 
sheet = wb.active
sheet.title = 'jay_song'
sheet['A1'] = '歌曲名'     # 加表头，给A1单元格赋值
sheet['B1'] = '所属专辑'   # 加表头，给B1单元格赋值
sheet['C1'] = '播放时长'   # 加表头，给C1单元格赋值
sheet['D1'] = '播放链接'   # 加表头，给D1单元格赋值
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':'周杰伦',
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    # 将参数封装为字典
    res_music = requests.get(url,params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        name = music['name']
        # 以name为键，查找歌曲名
        album = music['album']['name']
        # 查找专辑名
        time = str(music['interval'])
        # 查找播放时长
        link = 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n'
        # 查找播放链接
        sheet.append([name,album,time,link])
# 最后保存并命名这个Excel文件        
wb.save('Jay.xlsx')  