from flask import Flask
from flask_restful import Resource, Api, reqparse
from time import time
import werkzeug, os

app = Flask(__name__)
api = Api(app)
UPLOAD_FOLDER = '/app/static'
parser = reqparse.RequestParser()
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
parser.add_argument('files', type=werkzeug.datastructures.FileStorage, location='files', action='append')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class PhotoUpload(Resource):
    decorators=[]

    def post(self):
        data = parser.parse_args()
        if data['file'] == "":
            return {
                    'data':'',
                    'message':'No file found',
                    'status':'error'
                    }
        photo = data['file']

        if photo:
            filename = str(time()) + '.png'
            photo.save(os.path.join(UPLOAD_FOLDER,filename))
            return {
                    'data':'',
                    'message':'photo uploaded',
                    'status':'success'
                    }
        return {
                'data':'',
                'message':'Something when wrong',
                'status':'error'
                }

class MultiPhotoUpload(Resource):
    decorators=[]

    def post(self):
        data = parser.parse_args()
        if data['files'] == "":
            return {
                    'data':'',
                    'message':'No file found',
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
                    'message':'photos uploaded',
                    'status':'success'
                    }
        return {
                'data':'',
                'message':'Something when wrong',
                'status':'error'
                }


api.add_resource(HelloWorld, '/')
api.add_resource(PhotoUpload,'/upload')
api.add_resource(MultiPhotoUpload,'/multi_upload')

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5001, debug = True)
