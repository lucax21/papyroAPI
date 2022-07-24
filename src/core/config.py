import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")
    PROJECT_SERVER: str = os.getenv("PROJECT_SERVER")
    PROJECT_PORT: str = os.getenv("PROJECT_PORT")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASS: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    GOOGLE_API = os.getenv('GOOGLE_API')
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    TOKEN_ALGORITHM: str = os.getenv("TOKEN_ALGORITHM")
    REGISTRATION_TOKEN_LIFETIME = 60 * 60
    USER_TOKEN_LIFETIME = 30 * 60


    EMAIL_HOST = ('smtp.office365.com', 587)
    SSL = True
    EMAIL_HOST_USER: str = os.getenv("EMAIL_HOST")
    EMAIL_HOST_PASSWORD: str = os.getenv("EMAIL_HOST_PASSWORD")
    
settings = Settings()

