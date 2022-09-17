import smtplib
import email.message
import datetime

from src.utils.config import Settings

settings = Settings()

class Mailer:

    def enviar_email(content: str, subject: str, user_email: str):
    
        msg = email.message.Message()
        msg.set_payload(content)
        msg['Subject'] = subject
        msg['To'] = user_email
        msg['From'] = settings.EMAIL_HOST_USER

        s = smtplib.SMTP('smtp.office365.com: 587')
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(msg['From'], settings.EMAIL_HOST_PASSWORD) 
        s.send_message(msg)
        s.quit()


    def forgot_password(code_otp: str, user_email: str):

        msg = '''
        Codigo para recuperacao de senha: {}


        Data e hora da solicitacao: {}

        Obs. Este link tem validade de 5 minutos desde o pedido de troca de senha.
        '''.format(code_otp, datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

        
        
        Mailer.enviar_email(msg, 'Papyro Recuperacao de senha.', user_email)
