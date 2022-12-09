from flask import Flask, request

app = Flask(__name__)

users_ids = []


@app.route('/')
def index():
    return "Hello World!"


@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def users(user_id):

    if request.method == 'POST':
        users_ids.append(user_id)
        print(users_ids)
        return f"User with id: {user_id} has been created"

    if user_id not in users_ids:
        return "User not found", 404

    return f"User's id: {user_id}"


if __name__ == '__main__':
    app.run(debug=True)
