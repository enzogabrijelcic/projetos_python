from flask import Flask, render_template, request, redirect, url_for
import mariadb

app = Flask(__name__)

# Configurações do banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'formulario_db'

# Rota para exibir o formulário HTML
@app.route('/')
def formulario():
    return render_template('index.html')

#Rota para processar o aniversario
@app.route('/submit_date', methods= ['POST'])
def submit_date():
    aniversario = request.form['birthday']
    # Inserir dados no banco de dados
    connection = mariadb.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()
    # Executar comando SQL para inserir dados
    sql = "INSERT INTO aniversarios (data_nascimento) VALUES (?)"
    cursor.execute(sql, (aniversario,))
    connection.commit()
    # Fechar conexão com o banco de dados
    cursor.close()
    connection.close()

    # Redirecionar para página de sucesso ou outra página
    return redirect(url_for('sucesso'))


# Rota para processar o formulário
@app.route('/submit_formulario', methods=['POST'])
def submit_formulario():
    # Obter dados do formulário
    nome = request.form['nome']
    email = request.form['email']
    idade = request.form['idade']
    genero = request.form['genero']
    mensagem = request.form['mensagem']

    # Inserir dados no banco de dados
    connection = mariadb.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()

    # Executar comando SQL para inserir dados
    sql = "INSERT INTO usuarios (nome, email, idade, genero, mensagem) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (nome, email, idade, genero, mensagem))
    connection.commit()

    # Fechar conexão com o banco de dados
    cursor.close()
    connection.close()

    # Redirecionar para página de sucesso ou outra página
    return redirect(url_for('sucesso'))

# Rota para página de sucesso
@app.route('/sucesso')
def sucesso():
    return 'Dados inseridos com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)

