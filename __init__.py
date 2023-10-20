import re
from flask import Flask, jsonify, request
import ssl
import json
app = Flask(__name__)

@app.route("/", methods=["POST"])
def imprimir():
  response = {"status": 200}
  return jsonify(response)


@app.route("/webhook", methods=["POST"])
def imprimirPix():
  imprime = print(request.json)
  data = request.json
  with open('data.txt', 'a') as outfile:
      outfile.write("\n")
      json.dump(data, outfile)
  return jsonify(imprime)

@app.route("/pix", methods=["POST"])
def imprimirPix():
  imprime = print(request.json)
  data = request.json
  with open('data.txt', 'a') as outfile:
      outfile.write("\n")
      json.dump(data, outfile)
  return jsonify(imprime)


if __name__ == '__main__':
    app.run()
