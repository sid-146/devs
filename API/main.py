from flask import Flask, jsonify
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy



##! Error CODE
'''
# ! 200 working fine
# ! 201 Successful updatation
# ! 204 successful deletion
# ! 409 aleardy exiting ID
# !
'''


#create app
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///APIdatabase.db'

db = SQLAlchemy(app) 

class videoModel(db.Model):
    #! Define all the fields you wnt in your database
    ID = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(100), nullable = False)
    Views = db.Column(db.Integer, nullable = False)
    Likes = db.Column(db.Integer, nullable = False)
    
    def __repr__(self):
        return f"Video(name={Name}, views={Views}, likes={Likes})"


# ! line number 35 should be untouched othewise it will mess up with the databse
# db.create_all() #! DO NOT TOUCH IT !!!!!
##*####################################################################


Resource_Field = {
    "Name" : fields.String,
    "Likes" : fields.Integer,
    "Views" : fields.Integer,
    "ID": fields.Integer
}

videos_request_parser = reqparse.RequestParser()
# Cumpolsary and will produce error
videos_request_parser.add_argument("name", type= str, help="Name of video", required = True) 
# not cumpusolry requied (will not produce any error)
# Values which are not provided are given as None
videos_request_parser.add_argument("likes", type= int, help = "likes on the video")
videos_request_parser.add_argument("views", type=int, help= "Number of views on the video")


names = {
    "SK" :{"age": 20, "spicies":"hooman"},
    "Rio" :{"age": 3, "spicies": "Dog"},
    "oli": {"age": 2, "spicies": "Dog"}
}

videos = {

}

@app.route('/')
def default():
    return "Application is Running"

def videoIDnotValid(video_id):
    if video_id not in videos:
        abort(404,message= "Video ID not present...")

def videoIDExist(video_id):
    if video_id in videos:
        abort(409, message = "Video ID already exist")



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
    # To fetch data
    def get(self, video_id):
        videoIDnotValid(video_id=video_id)
        return videos[video_id]

    # To update data
    # @marshal_with(Resource_Field)
    def put(self, video_id):
        videoIDExist(video_id=video_id)
        args = videos_request_parser.parse_args()
        print(args)
        videos[video_id] = args
        return args, 201 # 201 showing successful updataion

    def delete(self, video_id):
        videoIDnotValid(video_id=video_id)
        del videos[video_id]
        return 204, " "
        pass

class NewVideoAPI(Resource):
    # To fetch data
    # marshal_converts videoModel object to json specifier
    @marshal_with(Resource_Field)
    def get(self, video_id):
        result = videoModel.query.filter_by(id= video_id).first()
        if not result:
            abort(404, message= "Video_ID not found...")
        print(type(result))
        return result
        # return jsonify(result), 200

    # To update data
    @marshal_with(Resource_Field)
    def put(self, video_id):
        args = videos_request_parser.parse_args()
        result = videoModel.query.filter_by(id= video_id).first()
        if result:
            abort(409, message= "Video_Id already exist...")
        tempVideo = videoModel(id= video_id, name = args['name'], views= args['views'], likes= args['likes'])
        db.session.add(tempVideo)
        db.session.commit()
        return videos[video_id], 201




### API RESOURCES ###

api.add_resource(Video, "/Video/<int:video_id>")
api.add_resource(HomePage, "/HP")
api.add_resource(param, "/para/<string:name>")

if __name__ == "__main__":
    app.run(debug= True)