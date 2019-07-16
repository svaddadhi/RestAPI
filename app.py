from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity 
app = Flask(__name__)
#this is to allow flask propagating exception even if debug is set to false on app
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'your_movies'
api=Api(app)

jwt = JWT(app, authenticate, identity)

movies=[]

class Movies(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('rating',
		type=float,
		required=True,
		help="Not leaving this part blank"
	)


	#we are going to iterate through the moviess and retrive the specific 
	#one that we want
	@jwt_required()
	def get(self, name):
		return {'item': next(filter(lambda x: x['name'] == name, movies), None)}


	#this is for creating the movies 
	def post(self, name):
		if next(filter(lambda x: x['name'] == name, movies), None) is not None:
			return {'message': "An item with name '{}' already exists.".format(name)}

		data = Movies.parser.parse_args()

		movie = {'name': name, 'rating': data['rating']}
		movies.append(movie)
		return movie
		
	@jwt_required()
	def put(self, name):
		data = Movies.parser.parse_args()
		movie = next(filter(lambda x: x['name'] == name, movies), None)
		if movie is None:
			movie = {'name': name, 'rating': data['rating']}
			movies.append(movie)
		else:
			movie.update(data)

	#deleting the movies
	@jwt_required()
	def delete(self, name):
		global movies
		movies = list(filter(lambda x: x['name'] != name, movies))
		return {'message': 'Item Deleted'}


class MovieList(Resource):
	def get(self):
		return {'movies': movies}


api.add_resource(Movies, '/movie/<string:name>')
api.add_resource(MovieList, '/movies')


if __name__ == '__main__':
	app.run(debug=True)












