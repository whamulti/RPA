import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações de credenciais
sender_email = "ricardo98365@gmail.com"
receiver_email = "gprilopes@gmail.com"
password = "vbdg tzyk bevv nukd" # Use Senha de App, não a senha normal

# Estrutura da mensagem
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = "Relatório Automático - RPA"
body = "Olá, segue o relatório em anexo."
message.attach(MIMEText(body, 'plain'))

# Conexão e Envio
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(message)
    print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro: {e}")
