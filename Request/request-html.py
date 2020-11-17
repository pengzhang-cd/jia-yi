# 引用requests库
import requests

# 下载https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html的html文件，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 把Response对象的内容以字符串的形式返回
dou_html = res.content
# 新建了一个文件 这个网站不太冷.html，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# html内容需要以二进制wb读写。你在学习open()函数时接触过它。
linshi = open('这个网站不太冷.html','wb')
# 获取dou_html的二进制内容
linshi.write(dou_html) 
# 关闭文件
linshi.close()