from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

app = Flask(__name__)

api=Api(app)

students=[]

class Student(Resource):
	def get(self, name):
		pass

	def post(self, name):
		pass

	def put(self, name):
		pass

	def delete(self, name):
		pass


class StudentList(Resource):
	def get(self):
		pass

