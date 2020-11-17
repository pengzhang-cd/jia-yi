# 引用requests库
import requests

# 下载文章《HTTP状态响应码》全部内容，我们得到一个对象，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
# 把Response对象的内容以字符串的形式返回
sta_code = res.text
# 新建了一个文件HTTP状态响应码.txt，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 文本内容需要以w读写。你在学习open()函数时接触过它。
code_text = open('HTTP状态响应码.txt','w')
# 获取sta_code的文本内容
code_text.write(sta_code) 
# 关闭文件
code_text.close()