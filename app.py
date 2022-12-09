from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/users/<user_id>')
def users(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        return "Validation error. User id should be integer.", 400

    return f"User id: {user_id}"


if __name__ == '__main__':
    app.run(debug=True)
