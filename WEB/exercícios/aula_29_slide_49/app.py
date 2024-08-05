from flask import Flask, request, jsonify
import mariadb
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso permitirá que todas as origens façam requisições para a API
app.config['SECRET_KEY'] = 'your_secret_key_here'


# Configurações do banco de dados (mariadb)
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'formulario_db'

@app.route('/register', methods=['POST'])
def register():
    connection = mariadb.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()
   
    data = request.get_json()
    nome = data.get('nome')
    senha  = data.get('senha')
    cpf = data.get('cpf')
   
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        if usuario[1] == nome:
            return jsonify({"message": "User already exists"}), 409
   
    hashed_password = generate_password_hash(senha, method='pbkdf2:sha256:600000')

     # Executar comando SQL para inserir dados
    sql = "INSERT INTO usuarios (nome,cpf,senha) VALUES (?,?,?)"
    cursor.execute(sql, (nome,cpf,hashed_password,))
    connection.commit()

    # Fechar conexão com o banco de dados
    cursor.close()
    connection.close()

    return jsonify({"message": "User registered successfully"}), 201




@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nome = data.get('nome')
    senha = data.get('senha')

    connection = mariadb.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    usuario_descoberto = None
    for usuario in usuarios:
        if usuario[1] == nome:
            usuario = usuario_descoberto
            break

    if not usuario_descoberto or not check_password_hash(usuario_descoberto[2], senha):
        return jsonify({"message": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


