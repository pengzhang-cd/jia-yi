# 引入requests库
import requests

# 发出请求，并把返回的结果放在变量res中
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
# 把Reponse对象的内容以二进制数据的形式返回
music = res.content
# 新建了一个文件pymusic.mp3，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 音频内容需要以二进制wb读写。你在学习open()函数时接触过它。
mu_mp3 = open('pymusic.mp3','wb')
# 获取music的二进制内容
mu_mp3.write(music) 
# 关闭文件
mu_mp3.close()