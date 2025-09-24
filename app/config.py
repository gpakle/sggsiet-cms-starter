import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 60 * 1024 * 1024  # 60MB

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/cms')
    MEDIA_PROVIDER = os.getenv('MEDIA_PROVIDER', 'local')
    MEDIA_FOLDER = os.getenv('MEDIA_FOLDER', os.path.join(BASE_DIR, '..', 'instance', 'media'))

class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    MEDIA_PROVIDER = os.getenv('MEDIA_PROVIDER', 'spaces')
    MEDIA_FOLDER = os.getenv('MEDIA_FOLDER', os.path.join(BASE_DIR, '..', 'instance', 'media'))
    # DO Spaces config
    DO_SPACE_REGION = os.getenv('DO_SPACE_REGION')
    DO_SPACE_ENDPOINT = os.getenv('DO_SPACE_ENDPOINT')
    DO_SPACE_BUCKET = os.getenv('DO_SPACE_BUCKET')
    DO_SPACE_KEY = os.getenv('DO_SPACE_KEY')
    DO_SPACE_SECRET = os.getenv('DO_SPACE_SECRET')
    DO_SPACE_BASE_URL = os.getenv('DO_SPACE_BASE_URL')
