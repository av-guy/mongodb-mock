import pymongo

from dotenv import load_dotenv
from mongo.conf import Configuration

load_dotenv()


class Customers:
    def __init__(self):
        self.__mongo = pymongo.MongoClient(Configuration.MONGO_DB_URL)
        self.__db = self.__create_db(name='boxdb')
        self.__customers = self.__create_column('customers')

    def __create_db(self, name='test'):
        return self.__mongo[name]

    def __create_column(self, column):
        return self.__db[column]

    @property
    def all(self):
        return self.__customers.find()

    def create(self, customer):
        self.__customers.insert_one(customer)
