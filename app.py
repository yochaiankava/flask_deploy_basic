from flask import Flask,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

ALL_STUDENTS = [{
    'id': 1,
    'name': 'Dan'
},
    {
    'id': 2,
    'name': 'Yochai'
}]


@app.route("/students")
def students():
    return jsonify(ALL_STUDENTS)


if __name__ == '__main__':
    app.run(debug=True)
