from tinydb import TinyDB, Query
import json

def insertCars(data):
    db=TinyDB('cars.json')
    d=json.loads(json.dumps(data))
    print(d)
    db.insert(d)

def fetchData(vin):
    datas=Query()
    db=TinyDB('cars.json')
    return json.dumps(db.search(datas.vin==vin))


def fetchAll():
    db=TinyDB('cars.json')
    return json.dumps(db.all())