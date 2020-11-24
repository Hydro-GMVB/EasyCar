# ESCOLA TÉCNICA ESTADUAL PORTO DIGITAL
# RECIFE, 03/11/2020
# ALUNO: CARLOS ALVAREZ & GUILHERME MOREIRA (2º A)
# -=-=-=-=-=- HELLO WORLD COM FLASK & -=-=-=-=-=-
# -=-=-=-=-=-     CONEXÃO SQLITE3     -=-=-=-=-=-
# ESTE CÓDIGO UTILIZOU COMO BASE OS SEGUINTES LINKS:
# https://docs.python.org/3/library/sqlite3.html
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# https://docs.google.com/document/d/1ulinGDvnOazmWhX9DeT7P7nG19XGabvueb1q215JtSc/edit
# https://docs.google.com/document/d/1ulinGDvnOazmWhX9DeT7P7nG19XGabvueb1q215JtSc/edit
# e M U I T O stackOverflow

#! Importando dependências
# Flask → Permite que a aplicação flask rode
# render_template → Permite o uso do JINJA no html
# jsonify → Converte uma string em JSON. Será o retorno do POST
# request → Permite que o usuário insira os valores do JSON do método POST
# json → Conjunto de métodos utilizados para o JSON
from flask import Flask, render_template, jsonify, request, json

# db → Funções do arquivo "db.py"
# sqlite3 → Conjunto de funções do sqlite
import db, sqlite3

# Inicializando o app do Flask com o diretorio para possivel html (escalabilidade)
app = Flask(__name__, template_folder="templates")

#! Método GET padrão (estilo "hello world!")
@app.route("/")
def hello_world():

    # Método de retornar um JINJA
    message = "Hello, Flask + Jinja 🐍"
    return render_template("index.html", message=message)

#! Método POST
@app.route("/cadastro", methods=["POST"])
def cadastro():

    # Esta função permite que o valor id_carros consiga
    # ser incrementado à medida que um valor é inserido no
    # banco de dados
    id_carros = db.getLastID()

    #! JSON
    # Cada veículo terá como chave o seu ID (autoincrementado automaticamente)
    # E as informações mais notáveis do veículo também serão inseridas nesta etapa
    informacoes = [{
        id_carros: {
            "modelo": request.json["modelo"],
            "quilometragem": request.json["quilometragem"],
            "ano": request.json["ano"],
            "placa": request.json["placa"],
            "condicao": request.json["condicao"],
            "preco": request.json["preco"]
        }
    }]
    db.jsonToDB(informacoes)
    
    return(jsonify(informacoes))

#! SEGUNDO MÉTODO GET
@app.route("/info")
def info():
    # É preciso abrir uma conexão neste arquivo. Se não houver,
    # o sqlite retornará um erro de threads
    conn = sqlite3.connect("db/carros.db")
    c = conn.cursor()

    # Esta atribuição permite que a variável data consiga
    # armazenar todos os valores da tabela carros
    data = c.execute("""
    SELECT * FROM carros;
    """).fetchall()
    
    # O que retorna é um json do banco de dados
    return jsonify(data)

#! Comando para fazer o flask rodar
# A opção debug faz com que o server seja atualizado a cada
# modificação
if __name__ == "__main__":
    app.run(debug=True, port=5000)