from flask_pymongo import PyMongo


def init_app(app):
    ""
    app.config["MONGO_URI"] = "mongodb://localhost:27017/raizen"
    mongo = PyMongo(app)
    return mongo.db