# 调用requests库
import requests 
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
# 返回一个response对象，赋值给res
res = requests.get('http://books.toscrape.com/')
# 把res解析为字符串
html = res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup( html,'html.parser')
# 通过匹配属性class='books'提取出我们想要的元素
# items = soup.find_all('div',class_='side_categories') 
items = soup.find('ul',class_='nav nav-list').find('li').find('ul').find_all('li')  
#print(items)
# 遍历列表items
for item in items:        
    # 在列表中的每个元素里，匹配标签<a>提取出数据               
    booktypes = item.find('a').text
    print(booktypes.strip())
   