from urllib.parse import quote
import os
from dotenv import load_dotenv, find_dotenv




class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "xxx"



class DevelopmentConfig(Config):
    # carrega .env.local caso exista
    base_path = os.path.abspath(os.path.dirname(__file__))

    local_env_path = os.path.join(base_path, '.env')
    if os.path.isfile(local_env_path):
        load_dotenv(find_dotenv(local_env_path))
    else:
        load_dotenv(find_dotenv())

    SECRET_KEY = "haksl"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEVELOPMENT = True
    DEBUG = os.getenv("DEBUG")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    ENV = os.getenv("ENV")
    TESTING = False
    
    #username = os.getenv("API_ESCRITURACAO_DB_USERNAME")
    #password = os.getenv("API_ESCRITURACAO_DB_PASSWORD")
    #db_name = os.getenv("API_ESCRITURACAO_DB_DATABASE")
    #password_encoded = quote(password)
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.getenv("API_ESCRITURACAO_DB_USERNAME")}:%s@{os.getenv("API_ESCRITURACAO_DB_HOST")}:3306/{os.getenv("API_ESCRITURACAO_DB_DATABASE")}' % quote(f'{os.getenv("API_ESCRITURACAO_DB_PASSWORD")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
    ALLOWED_EXTENSIONS = {"zip"}
    UPLOAD_FOLDER = f"{base_path}/lote/itau"
    SEND_FILE_MAX_AGE_DEFAULT = 0
    BASE_PATH = f"{base_path}"
    
 
   

  
   