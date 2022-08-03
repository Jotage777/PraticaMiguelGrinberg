from flask import Flask, request,render_template
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        user={'username': 'Gabriel'}
        posts=[
            {
                'author': {'username':'John'},
                'body': 'O dia amanheceu chuvoso em Campina Grande'
            },
            {
                'author': {'username':'Daniel'},
                'body':"Belo dia para programar"
            }
        ]
        return render_template('index.html',title = 'Home',user=user,posts=posts)


api.add_resource(Index,"/index")
if __name__ == "__main__":
    app.run(debug=True)