from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        return "Hello World"

api.add_resource(Index,"/index")
if __name__ == "__main__":
    app.run(debug=True)