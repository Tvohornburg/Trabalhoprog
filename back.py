from flask import Flask, json, jsonify, request
from classes import Jogador,Inimigo
from playhouse.shortcuts import model_to_dict 

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def comeco():
    return "Jogador: <a href=/listar_jogador> listar jogador</a>   Inimigo: <a href=/listar_inimigo> listar inimigo</a>"


@app.route('/listar_jogador')
def listar_jogador():
    jogador = list(map(model_to_dict, Jogador.select()))
    return jsonify({"Jogador" : jogador})


@app.route('/listar_inimigo')
def listar_inimigo():
    inimigo = list(map(model_to_dict, Inimigo.select()))
    return jsonify({"Inimigo" : inimigo})


app.run(debug=True, port=4999)