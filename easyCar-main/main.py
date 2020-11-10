'''
ESCOLA TÉCNICA ESTADUAL PORTO DIGITAL
RECIFE, 03/11/2020
ALUNO: CARLOS ALVAREZ & GUILHERME MOREIRA (2º A)

-=-=-=-=-=- HELLO WORLD COM FLASK & -=-=-=-=-=-
-=-=-=-=-=-     CONEXÃO SQLITE3     -=-=-=-=-=-

ESTE CÓDIGO UTILIZOU COMO BASE OS SEGUINTES LINKS:
https://docs.python.org/3/library/sqlite3.html
https://flask.palletsprojects.com/en/1.1.x/quickstart/
https://docs.google.com/document/d/1ulinGDvnOazmWhX9DeT7P7nG19XGabvueb1q215JtSc/edit
'''


#! Importando dependências
from flask import Flask, render_template, request
import sqlite3

# Inicializando o app do Flask com o diretorio para possivel html (escalabilidade)
app = Flask(__name__, template_folder="templates")

# Método GET padrão (estilo "hello world!")


@app.route("/")
def hello_world():
    message = "Hello, Flask + Jinja 🐍"
    return render_template("index.html", message=message)


# Comando para fazer o flask rodar
if __name__ == "__main__":
    app.run()

#! SQLITE
# Conexão e criação do arquivo do banco de dados
conn = sqlite3.connect("db/carros.db")
c = conn.cursor()

#! Função para o banco de dados
# A linha "c.execute(command)" permite que o dev consiga manipular a sua tabela facilmente.


def sqlcommand(command):
    c.execute(command)
    conn.commit()

# Esta função irá criar uma tabela padrão para o banco de dados


def defaultDB():
    c.execute('''
    CREATE TABLE IF NOT EXISTS carros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo VARCHAR(100) NOT NULL,
        quilometragem INT NOT NULL, 
        ano UNSIGNED INT NOT NULL,
        placa VARCHAR(8) NOT NULL,
        condicao VARCHAR(300),
        preco INT
    );
    ''')
    conn.commit()

# Esta função irá popular a tabela "estacionamento" com placeholders


def defaultValues():
    c.execute('''
    INSERT INTO carros(modelo, quilometragem, ano, placa, condicao, preco) VALUES(
        "Corsa", 128000, 2009, "XFG8433", "Ótimo estado", 20000
    );
    ''')
    conn.commit()
