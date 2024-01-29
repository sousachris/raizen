from weather.utils.json import JSONEncoder
from weather.models.weather import Weather

class WeatherRespository():

    def __init__(self, db):
        self.db = db
        pass

    def get_all(self):
        try:
            find = self.db.find({})
            results = []
            for data in find:
                results.append(Weather(**data).to_json())
            return {"count": len(results), "results": results}
        except Exception as e:
            raise Exception(e)

    def insert(self, data: dict):
        try:
            #data = JSONEncoder().encode(data)
            self.db.insert_one({"value": data})
            return data
        except Exception as e:
            raise Exception(e)
    
