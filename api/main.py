import os

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('users')


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


@app.route('/new_user', methods=['POST'])
@cross_origin()
def create_user():
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/new_clip/<user>', methods=['POST'])
@cross_origin()
def create_clip(user):
    try:
        data = request.json
        data['url'] = data['url'].split('/')[-1]
        todo_ref.document(user).collection('clips').add(data)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/list_clips/<user>', methods=['GET'])
@cross_origin()
def read(user):
    try:
        clips = [doc.to_dict() for doc in todo_ref.document(user).collection('clips').stream()]
        return jsonify(clips), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/update/<user>/<clip>', methods=['PUT'])
@cross_origin()
def update(user,clip):
    try:
        todo_ref.document(user).collection('clips').document(clip).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/delete/<user>/<clip>', methods=['DELETE'])
@cross_origin()
def delete(user,clip):
    try:
        print(user)
        print(clip)
        print(todo_ref.document(user).collections('clips'))
        todo_ref.document(user).collection('clips').document(clip).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))