from flask_restful import Resource, Api, reqparse
from flask import Flask
from time import time
import werkzeug, os

app = Flask(__name__)
api = Api(app)
UPLOAD_FOLDER = '/app/static'
parser = reqparse.RequestParser()
parser.add_argument('files', type=werkzeug.datastructures.FileStorage, location='files', action='append')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class MultiPhotoUpload(Resource):
    def post(self):
        data = parser.parse_args()
        if data['files'] == "":
            return {
                    'data':'',
                    'message':'No file sent',
                    'status':'error'
                    }
        photos = data['files']
        print(photos)
        if photos:
            for photo in photos:
                filename = str(time()) + '.png'
                photo.save(os.path.join(UPLOAD_FOLDER,filename))
            return {
                    'data':'',
                    'message':'Photos uploaded successfully!',
                    'status':'success'
                    }
        return {
                'data':'',
                'message':'Something went wrong!',
                'status':'error'
                }


api.add_resource(HelloWorld, '/')
api.add_resource(MultiPhotoUpload,'/multi_upload')

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5001, debug = True)
