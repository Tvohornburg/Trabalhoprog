from flask import Flask, json, jsonify, request
from classes import *
from playhouse.shortcuts import model_to_dict 

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def comeco():
    return "Jogador: <a href=/listar_jogador> listar jogador</a><br>   Inimigo: <a href=/listar_inimigo> listar inimigo</a><br>  NPC:  <a href=/listar_npc> listar NPC</a> <br>  Magia: <a href=/listar_magia> listar Magia</a>  <br> Item: <a href=/listar_item> listar Item</a>  <br> Arma: <a href=/listar_arma> listar Arma</a> <br> armadura: <a href=/listar_armadura> listar Armadura</a> <br> Poção: <a href=/listar_pocao> listar Poção</a> <br> Classe: <a href=/listar_classe> listar Classe</a> <br> Inventario: <a href=/listar_inventario> listar Inventario</a>         "  


@app.route('/listar_jogador')
def listar_jogador():
    jogador = list(map(model_to_dict, Jogador.select()))
    return jsonify({"Jogador" : jogador})


@app.route('/listar_inimigo')
def listar_inimigo():
    inimigo = list(map(model_to_dict, Inimigo.select()))
    return jsonify({"Inimigo" : inimigo})



@app.route('/listar_npc')
def listar_npc():
    npc = list(map(model_to_dict, Npc.select()))
    return jsonify({"NPC" : npc})



@app.route('/listar_magia')
def listar_magia():
    magia = list(map(model_to_dict, Magia.select()))
    return jsonify({"Magia" : magia})



@app.route('/listar_item')
def listar_item():
    item = list(map(model_to_dict, Item.select()))
    return jsonify({"Item" : item})



@app.route('/listar_arma')
def listar_arma():
    arma = list(map(model_to_dict, Arma.select()))
    return jsonify({"Inimigo" : arma})



@app.route('/listar_armadura')
def listar_armadura():
    armadura = list(map(model_to_dict, Armadura.select()))
    return jsonify({"Armadura" : armadura})



@app.route('/listar_pocao')
def listar_pocao():
    pocao = list(map(model_to_dict, Pocao.select()))
    return jsonify({"Poção" : pocao})



@app.route('/listar_classe')
def listar_classe():
    classe = list(map(model_to_dict, Classe.select()))
    return jsonify({"Classe" : classe})




@app.route('/listar_inventario')
def listar_inventario():
    inventario = list(map(model_to_dict, Inventario.select()))
    return jsonify({"Inventario" : inventario})



app.run(debug=True, port=4999)