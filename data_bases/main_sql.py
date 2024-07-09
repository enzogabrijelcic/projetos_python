import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('exemplo.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

# Inserir dados
cursor.execute('''
    INSERT INTO usuarios (nome, idade)
    VALUES (?, ?)
''', ('João', 30))

# Salvar (commit) as mudanças
conn.commit()

# Selecionar e exibir os dados
cursor.execute('SELECT * FROM usuarios')
for row in cursor.fetchall():
    print(row)

# Fechar a conexão
conn.close()


