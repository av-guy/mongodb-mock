import os

from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))


class Configuration:
    MONGO_DB_URL = os.environ.get('MONGO_DB_URL')
    MONGO_DB_HOST = os.environ.get('MONGO_DB_HOST')
    MONGO_DB_PORT = os.environ.get('MONGO_DB_PORT')
    PROJECT_PATH = 'C:\\Users\\t420\\dev\\slack-stuff'
