import requests
from bs4 import BeautifulSoup
url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get (url)
print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
# 用find_all()把所有符合要求的数据提取出来，并放在变量items里
items = soup.find_all('div') 
# 打印items的数据类型
print(type(items)) 
# 打印items
print(items)   