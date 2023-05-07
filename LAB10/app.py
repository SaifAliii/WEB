from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
from database import db
from resources import routes

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/mydb'
}
api = Api(app)
db.initialize_db(app)
routes.initialize_route(api)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
