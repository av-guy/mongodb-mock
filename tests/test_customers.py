import mongomock

from mongo.src.models import Customers
from mongo.conf import Configuration

MONGO_DB_HOST = Configuration.MONGO_DB_HOST
MONGO_DB_PORT = Configuration.MONGO_DB_PORT


@mongomock.patch(servers=((MONGO_DB_HOST, MONGO_DB_PORT),))
def test_find_all():
    database = Customers()
    database.create({
        'first': 'Jonathan',
        'last': 'Chaidez'
    })
    for customer in database.all:
        assert customer['first'] == 'Jonathan'
        assert customer['last'] == 'Chaidez'


@mongomock.patch(servers=((MONGO_DB_HOST, MONGO_DB_PORT),))
def test_find_all_fail():
    database = Customers()
    database.create({
        'first': 'Real',
        'last': 'Python'
    })
    for customer in database.all:
        assert customer['first'] == 'Jonathan'
        assert customer['last'] == 'Chaidez'
