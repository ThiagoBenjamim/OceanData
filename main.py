import smtplib
from email.message import EmailMessage
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random as ran
import keyboard
import pylab as p
import cv2
import time
from ultralytics import YOLO

SMTPPort = 465 # Foi a única porta que funcionou até agora
emailLogin = "ocean25data@gmail.com"#input("Digite o email do remetente:").strip() # Email do Remetente
emailSenha = "sbeu oygy wnsn wfxu"#input("Digite a senha do email remetente:").strip() # Senha de APP

try:
    # Criar conexão com servidor e entrar na conta
    s = smtplib.SMTP_SSL('Smtp.gmail.com', SMTPPort)
    s.login(emailLogin, emailSenha)
    print("Login realizado com sucesso!")

    # Coleta dos destinatários
    destinatarios = []
    num = 1#int(input("Digite quantos destinatários deseja ter:"))
    for i in range(num):
        destinatario = "yeshuarck@gmail.com"#input("Digite o email do destinatário " + str(i+1) + ":")
        destinatarios.append(destinatario)

    message = EmailMessage() # Criar objeto da Mensagem
    message['Subject'] = "Alerta ecológico!!!" # Assunto da Mensagem
    message['From'] = emailLogin # Remetente da Mensagem
    message.set_content("Este é um alerta ecológico automático.") # Conteúdo da Mensagem
    message['To'] = ", ".join(destinatarios) # Destinatários da Mensagem

    #s.send_message(message) # Enviar Mensagem
    #print("Email enviado com sucesso!") # Aviso de mensagem bem sucedida

except smtplib.SMTPAuthenticationError:
    print("Erro de autenticação: verifique seu email e senha.")
    print("Se você usa Gmail, pode precisar gerar uma senha de app.")
except smtplib.SMTPRecipientsRefused:
    print("Erro: destinatário(s) recusado(s). Verifique os emails informados.")
except smtplib.SMTPConnectError:
    print("Erro de conexão com o servidor SMTP.")
except smtplib.SMTPException as e:
    print(f"Erro ao tentar enviar email: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    try:
        pass#s.quit()  # Fechar conexão com servidor SMTP (em todos os casos)
    except:
        pass

#sbeu oygy wnsn wfxu

style.use("fivethirtyeight")

graf = p.figure()
dimen = graf.add_subplot(1, 1, 1)

def animar(i):
    xs = []
    ys = []
    for j in range(30):
        xs.append(j)
        ys.append(ran.randint(16, 19))
    if keyboard.is_pressed('t'):
        ys[:] = [40] * len(ys)
        s.send_message(message)
        print("Email enviado com sucesso!") # Aviso de mensagem bem sucedida
    dimen.clear()
    dimen.plot(xs, ys)
    dimen.set_ylabel('Temperatura(C°)')
    

ani = animation.FuncAnimation(graf, animar, interval=1000)

graf2 = p.figure()
dimen2 = graf2.add_subplot(1, 1, 1)

def animar2(i):
    xs = []
    ys = []
    for j in range(30):    
        xs.append(j)
        ys.append(ran.randint(3300, 3682))
    dimen2.clear()
    dimen2.plot(xs, ys)
    dimen2.set_ylabel('Profundidade(M)')
    

ani2 = animation.FuncAnimation(graf2, animar2, interval=1000)

graf3 = p.figure()
dimen3 = graf3.add_subplot(1, 1, 1)

def animar3(i):
    xs = []
    ys = []
    for j in range(30):    
        xs.append(j)
        ys.append(ran.randint(34, 36))
    dimen3.clear()
    dimen3.plot(xs, ys)
    dimen3.set_ylabel('Salinidade(g/Kg)')
    

ani3 = animation.FuncAnimation(graf3, animar3, interval=1000)

graf4 = p.figure()
dimen4 = graf4.add_subplot(1, 1, 1)

def animar4(i):
    xs = []
    ys = []
    for j in range(30):    
        xs.append(j)
        ys.append(ran.randint(80, 90))
    dimen4.clear()
    dimen4.plot(xs, ys)
    dimen4.set_ylabel('pH*10')

ani4 = animation.FuncAnimation(graf4, animar4, interval=1000)

plt.show()

