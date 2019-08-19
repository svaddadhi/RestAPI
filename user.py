import sqlite3
from flask_restful import Resource,  reqparse

class User(object):
	def __init__(self, id, username, password):
		self.id = id
		self.username = username
		self.password = password

	@classmethod
	def find_by_username(cls, username):
		connection = sqlite3.connect('movieDB.db')
		cursor = connection.cursor()

		query = "SELECT FROM users WHERE username=?"
		result = cursor.execute(query, (username,))

		row = result.fetchone()

		if row:
			user = cls(*row)
		else:
			user = None

		connection.close()

		return user

	def find_by_id(cls,  _id):
		connection = sqlite3.connect('movieDB.db')
		cursor = connection.cursor()

		query = "SELECT FROM users WHERE id=?"
		result = cursor.execute(query, (_id,))

		row = result.fetchone()

		if row:
			user = cls(*row)
		else:
			user = None

		connection.close()

		return user

