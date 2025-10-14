import cv2 as cv
import smtplib
from email.message import EmailMessage
import keyboard


SMTPPort = int(input("Digite o número da porta SMTP que deseja utilizar:"))
emailLogin = input("Digite o email do remetente:")
emailSenha = input("Digite a senha do email remetente:")

s = smtplib.SMTP_SSL('Smtp.gmail.com', SMTPPort)
s.login(emailLogin, emailSenha)

destinatarios = []
num = int(input("Digite quantos destinatários deseja ter:"))
for i in range(num):
    destinatario = input("Digite o nome do destinatário " + i + ":")
    destinatarios.append(destinatario)

message = EmailMessage()
message['Subject'] = "Alerta ecológico!!!"
message['From'] = emailLogin

while True: #loop de ações
