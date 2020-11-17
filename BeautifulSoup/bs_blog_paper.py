# 调用requests库
import requests 
# 调用BeautifulSoup库
from bs4 import BeautifulSoup 
# 返回一个response对象，赋值给res
res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
# 把res解析为字符串
html = res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser')
# 通过匹配标签‘article’提取出我们想要的元素
items = soup.find_all('article')  
# print(items)
# 遍历列表items
for item in items:        
    # 在列表中的每个元素里，匹配标签<a>提取出数据               
    paper_updata = item.find('time').text
    paper_title = item.find('h2').find('a').text
    paper_url = item.find('div').find('a')['href']
    print(paper_title.strip(),paper_url,paper_updata)
   