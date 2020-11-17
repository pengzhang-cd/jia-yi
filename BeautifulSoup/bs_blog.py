# 调用requests库
import requests 
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
# url = https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/
# 返回一个response对象，赋值给res
res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
# 把res解析为字符串
html = res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup( html,'html.parser')
# 通过匹配属性class='books'提取出我们想要的元素
items = soup.find_all(class_='comment byuser comment-author-forchangeman even thread-even depth-1')  
# print(items)
# 遍历列表items
for item in items:        
    # 在列表中的每个元素里，匹配属性class_='fn'提取出数据               
    authorvcard = item.find(class_='fn')
    # 在列表中的每个元素里，匹配属性标签'p'提取出数据 
    kind = item.find('p') 
    # 在列表中的每个元素里，匹配属性标签'time'提取出数据 
    uptime = item.find('time') 
    print(authorvcard.text,kind.text,uptime.text)