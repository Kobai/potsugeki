import os

from flask import Flask, request, jsonify, make_response
from firebase_admin import credentials, firestore, initialize_app
import shortuuid

app = Flask(__name__)

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('users')


def preflight():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


@app.route('/new_user', methods=['POST'])
def create_user():
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json)
        res = jsonify({"success": True})
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/new_clip/<user>', methods=['OPTIONS','POST'])
def create_clip(user):
    if request.method == 'OPTIONS':
        return preflight()
    try:
        data = request.json
        data['url'] = data['url'].split('/')[-1]
        data['id'] = shortuuid.uuid()
        todo_ref.document(user).collection('clips').document(data['id']).set(data)
        res = jsonify({"success": True})
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/list_clips/<user>', methods=['GET'])
def read(user):
    try:
        clips = [doc.to_dict() for doc in todo_ref.document(user).collection('clips').stream()]
        res = jsonify(clips)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/update/<user>/<clip>', methods=['PUT'])
def update(user,clip):
    try:
        todo_ref.document(user).collection('clips').document(clip).update(request.json)
        res = jsonify({"success": True})
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/delete/<user>/<clip>', methods=['OPTIONS','DELETE'])
def delete(user,clip):
    if request.method == 'OPTIONS':
        return preflight()
    try:
        todo_ref.document(user).collection('clips').document(clip).delete()
        res = jsonify({"success": True})
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    except Exception as e:
        return f"An Error Occured: {e}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))