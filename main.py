from flask import Flask
import pandas as pd

app = Flask(__name__)

tabela = pd.read_csv("advertising.csv")


@app.route("/")
def Vend():
    vendas = (tabela["Vendas"]).to_dict()
    return {"Vendas": vendas} 

@app.route("/Tv")
def televisao():
    tv = (tabela["TV"]).to_dict()
    return {"TV": tv} 

@app.route("/Radio")
def radi():
    radio = (tabela["Radio"]).to_dict()
    return {"Radio": radio}

@app.route("/Jornal")
def jorn():
    jornal = (tabela["Jornal"]).to_dict()
    return {"Jornal": jornal}

@app.route("/Campo/<campoEscolha>")
def campo(campoEscolha):
    campo = (tabela[campoEscolha]).to_dict()
    return {campoEscolha: campo}


app.run(host="0.0.0.0")
  


