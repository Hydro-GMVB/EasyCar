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

# Valores padrão para variáveis globais que serão utilizadas no projeto
carros = list()
id_carros = 0

# Inicializando o app do Flask com o diretorio para possivel html (escalabilidade)
app = Flask(__name__, template_folder="templates")

# Método GET padrão (estilo "hello world!")
@app.route("/")
def hello_world():

    # Método de retornar um JINJA
    message = "Hello, Flask + Jinja 🐍"
    return render_template("index.html", message=message)

# Método POST para enviar informações sobre os veículos
@app.route("/cadastro", methods=["POST"])
def cadastro():

    #! Variáveis globais
    # Estas variáveis serão lidas pelo escopo do código em geral
    # id_carros → permite que o ID seja atualizado
    # carros → permite que a lista com dicionários seja atualizada
    global id_carros
    global carros
    
    #! JSON
    # Cada veículo terá como chave o seu ID (autoincrementado automaticamente)
    # E as informações mais notáveis do veículo também serão inseridas nesta etapa
    informacoes = {
        id_carros: {
            "modelo": request.json["modelo"],
            "quilometragem": request.json["quilometragem"],
            "ano": request.json["ano"],
            "placa": request.json["placa"],
            "condicao": request.json["condicao"],
            "preco": request.json["preco"]
        }
    }

    # Autoincrementando o ID de cada veículo
    id_carros += 1

    #! Concatenando cada veículo numa lista
    # Em Python, o JSON será lido se a sua variável for do tipo list
    # Logo, será uma lista com um conjunto de dicionários (depois interpretados como JSON)
    # Este método permite que o JSON da aplicação acumule as entradas adicionadas
    carros.append(informacoes)

    # Salvando os JSON enviados num arquivo chamado "info.json"
    # Este arquivo permite que as informações do banco de dados sejam adicionadas no sqlite
    with open("carros.json", "w") as json_file:
        json.dump(carros, json_file)
        
    # Retorno do POST enviado (o que vai aparecer no POSTMAN)
    return(jsonify(carros))

#! SEGUNDO MÉTODO GET
@app.route("/info", methods=["POST", "GET"])
def info():
    id_pesquisa = request.form.get("id_pesquisa")
    id_pesquisa = "OKOIK"
    return "OJK"

#! Comando para fazer o flask rodar
# A opção debug faz com que o server seja atualizado a cada
# modificação
if __name__ == "__main__":
    app.run(debug = True, port = 5000)
