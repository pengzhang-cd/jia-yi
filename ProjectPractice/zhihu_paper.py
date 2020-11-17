import requests, bs4
import openpyxl 

wb = openpyxl.Workbook() 
sheet = wb.active
sheet.title = 'zhihu_zhangjiawei'
sheet['A1'] = 'Title'     # 加表头，给A1单元格赋值
sheet['B1'] = 'Summary'   # 加表头，给B1单元格赋值
sheet['C1'] = 'Link'   # 加表头，给C1单元格赋值

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for x in range(57):
    url = 'https://www.zhihu.com/people/zhang-jia-wei/posts?page='+ str(x+1) 
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find_all('div', class_="List-item",tabindex="0")
    for titles in bs:
        title = titles.find('h2').find('a').text
        summary = titles.find('div',class_="RichContent is-collapsed").find('div',class_="RichContent-inner").find('span').text
        link = titles.find('h2').find('a')['href']
        sheet.append([title,summary,link])
wb.save('zhihu_zhangjiawei.xlsx')