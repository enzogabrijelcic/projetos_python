import sqlite3

conn =""
def connect_data_base():#caminho do banco
    db_name='exemplo.db'
    global conn
    conn = sqlite3.connect(db_name)#comando que conecta e cria o banco
    create_table()

def create_table():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
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

def selecionar_usuarios():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    return cursor.fetchall()

def fechar_conexao():
    conn.close()

connect_data_base()
create_table()
inserir_usuario("abacate",35)
print(selecionar_usuarios())
fechar_conexao()

