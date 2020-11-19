# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header

# mail_host = 'smtp.163.com'
# mail_user = 'zhangpeng_cd'
# mail_pass = 'IMQJKKSNCJIXNITJ'

# sender = 'zhangpeng_cd@163.com'
# receivers = ['286434392@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
 
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
 
# try:
#     smtpObj = smtplib.SMTP() 
#     smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
#     smtpObj.login(mail_user,mail_pass)  
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print('邮件发送成功')
# except smtplib.SMTPException:
#     print('Error: 无法发送邮件')

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
 
my_sender = 'zhangpeng_cd@163.com'    # 发件人邮箱账号
my_pass = 'MYPLSVXPCLRYUKRI'              # 发件人邮箱密码
my_user = ['skywallkey@gmail.com', 'zhangpeng@sunportpower.com']     # 收件人邮箱账号，我这边发送给自己
def mail():
    ret = True
    try:
        text = '''这是一封来自python自动发送的邮件。
        这是在练习编程发送邮件。
        怎样丰富邮件的文字内容部分。
        人生苦短，我用python
        测试git 编辑发送add。commit'''
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = formataddr(["chris zhang",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = Header(",".join(my_user))              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"                # 邮件的主题，也可以说是标题
 
        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,my_user,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
 
ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")