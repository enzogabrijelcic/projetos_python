from flask import Flask, render_template, request, redirect, url_for
import mariadb

app = Flask(__name__)

# Configurações do banco de dados
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'hotel_db'

# Rota para exibir o cadastro HTML
@app.route('/')
def cadastro():
    return render_template('index.html')


# Rota para processar o cadastrp
@app.route('/submit_cadastro', methods=['POST'])
def submit_cadastro():
    # Obter dados do cadastro
    nome = request.form['nome']
    email = request.form['email']
    cpf = request.form['CPF']
    quarto = request.form['quarto']
    inicio = request.form['inicio']
    final = request.form['final']

    # Inserir dados no banco de dados
    connection = mariadb.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()

    # Executar comando SQL para inserir dados
    sql = "INSERT INTO clientes (nome, email, CPF, quarto, inicio, final) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (nome, email, cpf, quarto, inicio, final))
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