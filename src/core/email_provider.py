import smtplib
import email.message

from dotenv import load_dotenv
import os

load_dotenv()

def verificacao_email(user_email: str):
    corpo_email = """
    <p>Test1</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Papyro verificação de conta"
    msg['To'] = user_email
    msg['From'] = os.getenv("PAPYRO_EMAIL_CHECKER")
    password = os.getenv("PAPYRO_EMAIL_CHERCER_PASSWORD")
    msg.add_header('Content-Type','text/html')
    msg.set_payload(corpo_email)

    if not password:
        password = ""

    s = smtplib.SMTP('smtp.office365.com: 587')
    s.starttls()
    s.login(msg['From'], password) 
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    #print("Email enviado")
