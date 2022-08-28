import smtplib
import email.message

from src.core.config import Settings

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
        Codigo para recuperacao de senha: {}'''.format(code_otp)
        
        Mailer.enviar_email(msg, 'Papyro. Recuperacao de senha.', user_email)
