#import cv2 as cv
import smtplib
from email.message import EmailMessage
#import keyboard
#import plotly.express as px


SMTPPort = 465 # Foi a única porta que funcionou até agora
emailLogin = input("Digite o email do remetente:") # Email do Remetente
emailSenha = input("Digite a senha do email remetente:") # Senha de APP

try:
    # Criar conexão com servidor e entrar na conta
    s = smtplib.SMTP_SSL('Smtp.gmail.com', SMTPPort)
    s.login(emailLogin, emailSenha)
    print("Login realizado com sucesso!")

    # Coleta dos destinatários
    destinatarios = []
    num = int(input("Digite quantos destinatários deseja ter:"))
    for i in range(num):
        destinatario = input("Digite o email do destinatário " + str(i+1) + ":")
        destinatarios.append(destinatario)

    message = EmailMessage() # Criar objeto da Mensagem
    message['Subject'] = "Alerta ecológico!!!" # Assunto da Mensagem
    message['From'] = emailLogin # Remetente da Mensagem
    message.set_content("Este é um alerta ecológico automático.") # Conteúdo da Mensagem
    message['To'] = ", ".join(destinatarios) # Destinatários da Mensagem

    s.send_message(message) # Enviar Mensagem
    print("Email enviado com sucesso!") # Aviso de mensagem bem sucedida

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
        s.quit()  # Fechar conexão com servidor SMTP (em todos os casos)
    except:
        pass

#df = px.data.gapminder().query("continent=='Oceania'")
#fig = px.line(df, x="year", y="lifeExp", color='country')
#fig.show()