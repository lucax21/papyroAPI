import smtplib
import email.message

from src.core.config import Settings

settings = Settings()

class Mailer:

    # @staticmethod
    def enviar_email(content: str, subject: str, user_email: str):
    
        msg = email.message.Message()
        msg.set_payload(content)
        msg['Subject'] = subject
        msg['To'] = user_email
        msg['From'] = settings.EMAIL_HOST_USER

        # msg.add_header('Content-Type','text/html')

        s = smtplib.SMTP('smtp.office365.com: 587')
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(msg['From'], settings.EMAIL_HOST_PASSWORD) 
        # s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        s.send_message(msg)
        s.quit()
        #print("Email enviado")

    # @staticmethod
    def enviar_email_confirmacao(token: str, user_email: str):

        # para rodar no docker
        #confirmacao_url = f'http://{settings.PROJECT_SERVER}:{settings.PROJECT_PORT}/usuarios/verificacao/{token}'

        # para rodar no gcloud
        confirmacao_url = f'http://{settings.PROJECT_SERVER}/usuarios/verificacao/{token}'


        mensagem = '''
        Por favor, confirme sua cadastro no papyro: {}'''.format(confirmacao_url)
        
        Mailer.enviar_email(mensagem, 'Confirme sua cadastro no papyro', user_email)