import requests, bs4
import openpyxl 
wb = openpyxl.Workbook() 
sheet = wb.active
sheet.title = 'douban_movie'
sheet['A1'] = 'NO.'     # 加表头，给A1单元格赋值
sheet['B1'] = '电影名'   # 加表头，给B1单元格赋值
sheet['C1'] = '评分'   # 加表头，给C1单元格赋值
sheet['D1'] = '推荐语'   # 加表头，给D1单元格赋值
sheet['E1'] = '网址链接'   # 加表头，给E1单元格赋值
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
        else:
            tes = ''
       
        url_movie = titles.find('a')['href']
        sheet.append([num,title,comment,tes,url_movie])
wb.save('doubanmovie250.xlsx')