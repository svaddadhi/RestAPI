from werkzeug.security import safe_str_cmp
from user import User

users = [
	User(1, 'user1', 'abcxyz'),
	User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userif_table = {u.id: u for u in users}

def authenticate(user, password):
	user = username_table.get(username, None)
	if user and safe_str_cmp(user.password, password):
		return None

def identity(payload):
	user_id = payload['identity']
	return userid_table.get(user_id, None)