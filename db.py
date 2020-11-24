import sqlite3

#! CRIAÇÃO DA TABELA
# Esta função irá criar uma tabela padrão para o banco de dados
# Ela terá um ID autoincrementado automaticamente
def defaultTable():
    conn = sqlite3.connect("db/carros.db")
    c = conn.cursor()
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

    # Esta linha irá SALVAR a tabela após as suas alterações
    conn.commit()

#! PLACEHOLDER
# Esta função irá popular a tabela "estacionamento" com placeholders
# Seu único propósito é servir de base para outras funções
def defaultValues():
    conn = sqlite3.connect("db/carros.db")
    c = conn.cursor()
    conn = sqlite3.connect("db/carros.db")
    c = conn.cursor()
    c.execute('''
    INSERT INTO carros(modelo, quilometragem, ano, placa, condicao, preco) VALUES(
        "Corsa", 128000, 2009, "XFG8433", "Ótimo estado", 20000
    );
    ''')
    conn.commit()

#! ADICIONAR O JSON NO DB
# A fnução mais importante deste projeto, pois ela permite
# que o JSON adicionado no POST seja adicionado no banco de dados
def jsonToDB(data):
    conn = sqlite3.connect("db/carros.db")
    c = conn.cursor()

    # Estrutura que permite a inserção de valores do JSON na tabela
    # Os 2 loops permitem que o JSON seja interpretado como um dict
    for id_carros in data:
        for info in id_carros.values():

            #! Adição dos valores
            # Esta linha de código permite que os valores de cada chave
            # do JSON sejam adicionados à tabela
            c.execute('''
            INSERT INTO carros(modelo, quilometragem, ano, placa, condicao, preco) VALUES(
                ?, ?, ?, ?, ?, ?
            );''', (
                info["modelo"],
                info["quilometragem"],
                info["ano"],
                info["placa"],
                info["condicao"],
                info["preco"]
            )
            )

            conn.commit()

def getLastID():
    conn = sqlite3.connect("db/carros.db")
    c = conn.cursor()

    # Variável last_id receberá o valor do último ID
    last_id = c.execute("""
    SELECT id FROM carros ORDER BY id DESC LIMIT 1;
    """).fetchone()
    
    # Por padrão, fetchone() retorna uma tupla, a linha abaixo
    # irá retornar o valor dentro da tupla
    return last_id[0]