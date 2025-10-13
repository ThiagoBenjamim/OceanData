import cv2 as cv
import smtplib
from email.message import EmailMessage


SMTPPort = int(input("Digite o número da porta SMTP que deseja utilizar:"))
emailLogin = input("Digite o email do remetente:")
emailSenha = input("Digite a senha do email remetente:")

s = smtplib.SMTP_SSL('Smtp.gmail.com', SMTPPort)
s.login(emailLogin, emailSenha)

num = int(input("Digite quantos destinatários deseja ter:"))
for i in range(num):
    

message = EmailMessage()
message.set_content()
message['Subject'] = ""
message['From'] = ""
message['To'] = ""


s.send_message(message)