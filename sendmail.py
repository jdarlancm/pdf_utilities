import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE

# Endereço de email do remetente e senha
email_sender = 'seu_email@gmail.com'
email_sender_password = 'sua_senha'

# Endereço de email do destinatário
email_receiver = 'destinatario@email.com'

# Cria o objeto de mensagem multipart
msg = MIMEMultipart()

# Adiciona o arquivo PDF como um anexo à mensagem
filename = 'pagina1.pdf'
with open(filename, 'rb') as f:
    attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str(filename))
    msg.attach(attach)

# Configura a mensagem
msg['From'] = email_sender
msg['To'] = COMMASPACE.join([email_receiver])
msg['Subject'] = 'Arquivo PDF anexado'

# Conecta com o servidor SMTP do Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_sender, email_sender_password)

# Envia a mensagem
server.sendmail(email_sender, [email_receiver], msg.as_string())
server.quit()
