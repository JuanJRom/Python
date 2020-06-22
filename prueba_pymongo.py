from pymongo import MongoClient

client = MongoClient()

db = client['pymongodb']

people = db['people']

person = {
    'name': 'Juan',
    'date': '1991/02/11',
    'place': 'Jalisco'
}

person1 = {
    'name': 'Blanca',
    'date': '1993/08/14',
    'place': 'Jalisco'
}

#people.insert_one(person)
#people.insert_one(person1)

#bucle = people.find_one_and_delete({'Name': 'Blanca'})

