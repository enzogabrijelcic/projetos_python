#Crie um objeto na sua mente
#faça uma tabela no banco para esse objeto.
#Cadastre uma pequena lista desse objeto
#Liste esse objeto.

import sqlite3

conn =""
def connect_data_base():#caminho do banco
    db_name='album.db'
    global conn
    conn = sqlite3.connect(db_name)#comando que conecta e cria o banco
    create_table_usuarios()
    create_table_albuns()

def create_table_albuns():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS albuns (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(50) NOT NULL ,
            artista VARCHAR(50),
            ano VARCHAR(50),
            gravadora VARCHAR(50),
            estilo VARCHAR(50)            
        )
    ''')
    conn.commit()


def create_table_usuarios():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(50) NOT NULL ,
            idade INTEGER
        )
    ''')
    conn.commit()

def inserir_usuario(nome, idade):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES (?, ?)
    ''', (nome, idade))
    conn.commit()

def inserir_album(nome, artista, ano, gravadora, estilo):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO albuns (nome, artista, ano, gravadora, estilo)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, artista, ano, gravadora, estilo))
    conn.commit()


def selecionar_usuarios():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(f"Usuario: {usuario}\n")

def selecionar_album():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM albuns')
    albuns = cursor.fetchall()
    for album in albuns:
        print(f"Album: {album}\n")

def fechar_conexao():
    conn.close()

def list_all_tables():
    cursor = conn.cursor()
    # Listar todas as tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()
    for tabela in tabelas:
        print("TABELA: ", tabela[0])
    conn.commit()



connect_data_base()

list_all_tables()

inserir_album('universo em desencanto', 'Tim Maia', 1970, 'Seroma', 'Soul')
selecionar_album()
fechar_conexao()



