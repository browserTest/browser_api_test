import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
import logging
from config.config import *


def send_email(file_dir, mailto):

    """获取报告内容"""
    with open(file_dir, encoding='utf-8') as f:
        file_context = f.read()

    msg = MIMEMultipart()     # 混合MIME格式
    msg.attach(MIMEText(file_context, 'html', 'utf-8'))     # 添加html格式邮件正文


    """组装email的header"""
    msg['from'] = email_sender
    msg['To'] = ",".join(mailto)
    msg['Subject'] = Header(email_subject, 'utf-8')

    """添加附件"""
    attachment = MIMEText(open(file_dir, 'rb').read(), 'base64', 'utf-8')
    attachment["Content-Disposition"] = 'attachment; filename= report.html'
    msg.attach(attachment)

    """连接smtp服务器，并发送邮件"""
    try:
        server = smtplib.SMTP(smtp_server)
        server.sendmail(smtp_sender, mailto, msg.as_string())
    except Exception as e:
        logging.error(str(e))
    finally:
        server.close()


