# 引用requests库
import requests

# 下载《三国演义》第一回，我们得到一个对象，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# 把Response对象的内容以字符串的形式返回
novel=res.text
# 新建了一个文件sanguo.tet，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
nov_sanguo = open('sanguo.txt','w')
# 获取novel的文本内容
nov_sanguo.write(novel) 
# 关闭文件
nov_sanguo.close()
# 现在，可以打印小说了，但考虑到整章太长，只输出800字看看就好。在关于列表的知识那里，你学过[:800]的用法。
print(novel[:800])