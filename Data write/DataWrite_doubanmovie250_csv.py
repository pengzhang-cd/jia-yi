import requests, bs4
import csv 
csv_file = open('doubanmovie250.csv','w',newline = '')
writer = csv.writer(csv_file)
writer.writerow(['NO.','电影名','评分','简介','网址链接'])

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
        writer.writerow([num,title,comment,tes,url_movie])
csv_file.close()