from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse


#create app

app = Flask(__name__)
api = Api(app)

videos_request_parser = reqparse.RequestParser()

# Cumpolsary and will produce error
videos_request_parser.add_argument("name", type= str, help="Name of video")

# not cumpusolry requied (will not produce any error)
videos_request_parser.add_argument("likes", type= int, help = "likes on the video")
videos_request_parser.add_argument("views", type=int, help= "Number of views on the video")


names = {
    "SK" :{"age": 20, "spicies":"hooman"},
    "Rio" :{"age": 3, "spicies": "Dog"},
    "Oli": {"age": 2, "spicies": "Dog"}
}

videos = {

}

# Resourse Helps in handling requests (GET, POST, PUT etc)
class HomePage(Resource):
    def get(self):
        return {"Value": "Home Page"}

    def post(self):
        return {"Data2": "Data posted"}


class param(Resource):
    # def get(self, name, age):
        # return ({"name": name, "age": age})
    
    #! Finding particular ID
    def get(self, name):
        return names[name]

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self):
        return None


### API RESOURCES ###


api.add_resource(Video, "/Video/<int:video_id>")
api.add_resource(HomePage, "/HP")
api.add_resource(param, "/para/<string:name>")

if __name__ == "__main__":
    app.run(debug= True)