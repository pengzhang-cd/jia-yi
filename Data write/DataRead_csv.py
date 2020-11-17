# 导入csv模块
import csv
# 用open()打开“demo.csv”文件，'r'是read读取模式，newline=''是避免出现两倍行距。encoding='utf-8'能避免编码问题导致的报错或乱码。
csv_file = open('demo.csv','r',newline='',encoding='utf-8')
# 用csv.reader()函数创建一个reader对象
reader = csv.reader(csv_file)
# print(type(reader))
# 用for循环遍历reader对象的每一行。打印row，就能读取出“demo.csv”文件里的内容。
for row in reader:
    print(row)
    print(type(row))
csv_file.close()