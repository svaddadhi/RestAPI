from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

app = Flask(__name__)

api=Api(app)

movies=[]

class Movies(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument()
	#we are going to iterate through the moviess and retrive the specific 
	#one that we want

	def get(self, name):
		for movie in movies:
			if name == movie['name']:
				return movie, 200
		return "Student not found", 404


	#this is for creating the movies 
	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None) is not None:
			return {'message': "An item with name '{}' already exists.".format(name)}
		

	def put(self, name):
		pass

	def delete(self, name):
		pass


class StudentList(Resource):
	def get(self):
		pass

