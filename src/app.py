from flask import Flask
app = Flask(__name__)

@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'


# # def hello_world():
#     # supongamos que tienes some_data (cierta información) en una variable json
#     some_data = { "name": "Bobby", "lastname": "Rixer" }

#     # puedes convertir esa variable en un string json así
#     json_text = flask.jsonify(some_data)

#     # y luego puedes retornarla (return) en el response body así:
#     return json_text




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)