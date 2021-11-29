from flask import Flask,jsonify
from flask import request


app = Flask(__name__)


objects = [
    { "objects": "My first object", "objectID": True },
    { "objects": "My second object", "objectID": True }
]


@app.route('/objects', methods=['GET'])
def get_objects():
  return jsonify(objects)


# @app.route('/objects', methods=['POST'])
# def add_new_object():
#     request_body = request.get_json(force=True)
#     objects.append(request_body)
#     return jsonify(objects)








if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

# @app.route('/blabla', methods=['GET'])
# def hello_world():
#     return 'Hello, World!'


# # def hello_world():
#     # supongamos que tienes some_data (cierta información) en una variable json
#     some_data = { "name": "Bobby", "lastname": "Rixer" }

#     # puedes convertir esa variable en un string json así
#     json_text = flask.jsonify(some_data)

#     # y luego puedes retornarla (return) en el response body así:
#     return json_text

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     request_body = request.data
#     print("Incoming request with the following body", request_body)
#     return 'Response for the POST todo'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)