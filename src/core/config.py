import os
import smtplib
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "Papyro"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_SERVER: str = os.getenv("PROJECT_SERVER")
    PROJECT_PORT: str = os.getenv("PROJECT_PORT")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASS: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


    SECRET_KEY: str = os.getenv("SECRET_KEY")
    TOKEN_ALGORITHM = 'HS256'
    REGISTRATION_TOKEN_LIFETIME = 60 * 60
    USER_TOKEN_LIFETIME = 30 * 60


    EMAIL_HOST = ('smtp.office365.com', 587)
    SSL = True
    EMAIL_HOST_USER ='papyroAPI@outlook.com'
    EMAIL_HOST_PASSWORD = 'P4pYr0123'

    
settings = Settings()

