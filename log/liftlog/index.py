from flask import Flask, jsonify, request

app= Flask(__name__)

sets = [
    { 'repetitions': 15, 'weight': 130, 'time': 60 }
]




@app.route("/sets")
def get_sets():
    return jsonify(sets)


@app.route('/sets', methods=['POST'])
def add_sets():
    sets.append(request.get_json())
    return '', 204