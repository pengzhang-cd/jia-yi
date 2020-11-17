# 调用requests库
import requests 
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
# 返回一个response对象，赋值给res
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
# 把res解析为字符串
html = res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup( html,'html.parser')
# 通过匹配属性class='books'提取出我们想要的元素
# items = soup.find_all('div',class_='side_categories') 
items = soup.find('ol').find_all('li') 
#print(items)
# 遍历列表items
for item in items:        
    # 在列表中的每个元素里，匹配标签<a>提取出数据               
    bookname = item.find('h3').find('a')['title']
    bookrating = item.find('p')['class'][1]
    bookprice = item.find('div',class_='product_price').find('p').text
    print(bookname.strip(),bookrating,bookprice.strip())
   