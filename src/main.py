from mongo.src.models import Customers


def initialize():
    customers = Customers()
    customers.create({
        'first': 'Jonathan',
        'last': 'Chaidez'
    })
    for customer in customers.all:
        print(customer)
