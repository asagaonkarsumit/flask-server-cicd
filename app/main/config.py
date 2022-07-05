import os
import logging
from logging.handlers import TimedRotatingFileHandler
from re import TEMPLATE


if not os.path.exists("log/"):
    os.makedirs("log")

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s  %(name)s %(threadName)s :- %(message)s")

handler = TimedRotatingFileHandler(
    'log/app.log', when="midnight", interval=1, encoding='utf8')

handler.suffix = "%Y-%m-%d_%H-%M-%S"
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)




ssl_logger = logging.getLogger(__name__)
ssl_logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(message)s')

file_handler = logging.FileHandler('log/ssl2.log')
file_handler.setFormatter(formatter)

ssl_logger.addHandler(file_handler)



class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False



MIN_SUB_ARTICLE_COUNT = 5
MIN_DEC_LENGTH = 20
MIN_TAG_LENGTH = 2
MIN_TITLE_LENGTH = 5
img_base_width = 680
img_base_height = 680
TEMPLATE = 'templates'


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    SERVER_IP = '35.192.207.77'
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'testdb'
    DATABASE_PASSWORD = 'admin123'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TYPE = logging.DEBUG
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"
    MAIL_USERNAME = 'info.hostinr'
    MAIL_PASSWORD = 'mgtxkgegecjxqkjw'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    PAGE = 1
    LIMIT = 10
    DEFAULT_COUNTRY = "US"
    bucket_base_url = "https://storage.googleapis.com/cur-layout-dev-data/"
    BUCKET_NAME = "cur-layout-dev-data"
    remote_image_page_directory = "Images/"  # with /
    dafault_widgit_blank_image = "https://storage.googleapis.com/cur-layout-dev-data/sliderImage.png"
    LOGO = "Logo/"
    gtag = "G-1B2J968VCN"
    THUMBNAIL = "Thumbnail/"
    CLIENT_ID_PRODUCTION = "436819105815-pns2vtis52sbnilbt1fsgj7psl5ujtk3.apps.googleusercontent.com"
    CLIENT_ID_DEVELOPMENT = "240891439748-8sqgqfurlmg3v9d97hk5smtjeqh54v2i.apps.googleusercontent.com"
    EXTENSION_CLIENT_ID_DEVELOPMENT = "764686557098-6ufl650l5ink1o2d66vbcvhbj1gtgeks.apps.googleusercontent.com"
    EXTENSION_CLIENT_ID_PRODUCTION = "306831557249-9q5s6r5128rmf58nbpeqcmv6r4sa15al.apps.googleusercontent.com"
    DOMAIN_NAME = ".nmedia2.com"
    EMAIL_INVITATION = "https://nmedia2.com/new/user/"
    EMAIL_VERIFICATION_DOMAIN = "https://nmedia2.com/confirm-email/"
    HTML_GCP_REMOTE_FOLDER = "page"


class TestingConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    SERVER_IP = ''
    ENV = 'development'
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'testdb1'
    DATABASE_PASSWORD = 'admin123'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_DEFAULT_SENDER = "curiousreadapp@gmail.com"
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"
    MAIL_USERNAME = 'info.hostinr'
    MAIL_PASSWORD = 'mgtxkgegecjxqkjw'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    PAGE = 1
    LIMIT = 10
    DEFAULT_COUNTRY = "US"
    bucket_base_url = "https://storage.googleapis.com/cur-layout-dev-data/"
    BUCKET_NAME = "cur-layout-dev-data"
    remote_image_page_directory = "Images/"  # with /
    dafault_widgit_blank_image = "https://storage.googleapis.com/cur-layout-dev-data/sliderImage.png"
    LOGO = "Logo/"
    gtag = "G-1B2J968VCN"
    THUMBNAIL = "Thumbnail/"
    CLIENT_ID_PRODUCTION = "436819105815-pns2vtis52sbnilbt1fsgj7psl5ujtk3.apps.googleusercontent.com"
    CLIENT_ID_DEVELOPMENT = "240891439748-8sqgqfurlmg3v9d97hk5smtjeqh54v2i.apps.googleusercontent.com"
    EXTENSION_CLIENT_ID_DEVELOPMENT = "764686557098-6ufl650l5ink1o2d66vbcvhbj1gtgeks.apps.googleusercontent.com"
    EXTENSION_CLIENT_ID_PRODUCTION = "306831557249-9q5s6r5128rmf58nbpeqcmv6r4sa15al.apps.googleusercontent.com"
    DOMAIN_NAME = ".nmedia2.com"
    EMAIL_INVITATION = "https://nmedia2.com/new/user/"
    EMAIL_VERIFICATION_DOMAIN = "https://nmedia2.com/confirm-email/"
    HTML_GCP_REMOTE_FOLDER = "page"


class ProductionConfig(Config):
    """
    Production Environment Config FIle Configuration
    Environment Required Variable:
        variable         :     operation                 :      example
    ==================================================================================================================
        DATABASE_NAME    : export name                   :       "mydb"
        DATABASE_PASSWORD: export DATABASE_USER password :       "xyz"
        DATABASE_URI     : export databse URI            :       IP Address
        DATABASE_PORT    : export port                   :       "5432"
    ==================================================================================================================
    """
    TESTING = False
    DEBUG = False
    SERVER_IP = '35.192.207.77'
    ENV = 'production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_URI = os.environ.get("DATABASE_URI")
    DATABASE_PORT = os.environ.get("DATABASE_PORT")
    MAIL_DEFAULT_SENDER = "curiousreadapp@gmail.com"
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"
    MAIL_USERNAME = 'info.hostinr'
    MAIL_PASSWORD = 'mgtxkgegecjxqkjw'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    PAGE = 1
    LIMIT = 10
    DEFAULT_COUNTRY = "US"
    bucket_base_url = "https://storage.googleapis.com/cur-layout-prod-data/"
    BUCKET_NAME = "cur-layout-prod-data"
    remote_image_page_directory = "Images/"  # with /
    dafault_widgit_blank_image = "https://storage.googleapis.com/cur-layout-dev-data/sliderImage.png"
    LOGO = "Logo/"
    gtag = "G-1B2J968VCN"
    THUMBNAIL = "Thumbnail/"
    CLIENT_ID_PRODUCTION = "436819105815-pns2vtis52sbnilbt1fsgj7psl5ujtk3.apps.googleusercontent.com"
    CLIENT_ID_DEVELOPMENT = "240891439748-8sqgqfurlmg3v9d97hk5smtjeqh54v2i.apps.googleusercontent.com"
    EXTENSION_CLIENT_ID_DEVELOPMENT = "764686557098-6ufl650l5ink1o2d66vbcvhbj1gtgeks.apps.googleusercontent.com"
    EXTENSION_CLIENT_ID_PRODUCTION = "306831557249-9q5s6r5128rmf58nbpeqcmv6r4sa15al.apps.googleusercontent.com"
    DOMAIN_NAME = ".storyeapp.com"
    EMAIL_INVITATION = "https://storyeapp.com/new/user/"
    EMAIL_VERIFICATION_DOMAIN = "https://storyeapp.com/confirm-email/"
    HTML_GCP_REMOTE_FOLDER = "page"



config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
