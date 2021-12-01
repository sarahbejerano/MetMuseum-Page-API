from flask import Flask, jsonify

app = Flask(__name__)

from metmuseum import objects

# creando una ruta, es decir que cuando se visite la ruta /objects se va a ejecutar la funcion.
# queremos que retorne en Jsonify (formato de intercambio de datos ideal). desde la ruta decidimos tb que tipo de metodo utilizamos 

@app.route('/objects', methods=["GET"])
def getobjects():
  return jsonify(objects)





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000, debug=True)