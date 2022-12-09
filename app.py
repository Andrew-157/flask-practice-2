from flask import Flask, request

app = Flask(__name__)

users_ids = {}


@app.route('/')
def index():
    return "Hello World!"


@app.route('/users/<int:user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users(user_id):

    if request.method == 'POST':

        if user_id in users_ids:
            return f"User with {user_id} already exists", 409

        users_ids[user_id] = request.json

        return f"User with id: {user_id} has been created"

    if user_id not in users_ids:
        return "User not found", 404

    if request.method == 'PUT':

        users_ids[user_id] = request.json

    if request.method == 'DELETE':

        del users_ids[user_id]
        return f"User with id: {user_id} was deleted"

    return f"User's id: {user_id}, user's info: {users_ids[user_id]}"


if __name__ == '__main__':
    app.run(debug=True)
