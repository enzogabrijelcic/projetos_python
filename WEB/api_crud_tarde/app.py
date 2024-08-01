#Arquivo principal onde a aplicação Flask é iniciada.
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso permitirá que todas as origens façam requisições para a API
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Simulando um banco de dados com dicionário
users_db = {}
pessoa = {"nome":"", "senha":"", "cpf":""}
count = 0

@app.route('/register', methods=['POST'])
def register():
    global count
    data = request.get_json()
    nome = data.get('nome')
    senha = data.get('senha')
    cpf = data.get('cpf')
    
    for chave, valor in users_db.items():
        if valor["nome"] == nome:
            if "nome"== valor:
                return jsonify({"message": "User already exists"}), 409
   
    hashed_password = generate_password_hash(senha, method='pbkdf2:sha256:600000')
    count = count+1
    users_db[f"pessoa{count}"] = {"nome": nome, 'cpf': cpf, 'senha': hashed_password} 
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nome = data.get('nome')
    senha = data.get('senha')
    cpf = data.get('cpf')
    
   
    user_password = users_db.get(nome)
    if not user_password or not check_password_hash(user_password, senha):
        return jsonify({"message": "Invalid username or password"}), 401
   
    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    app.run(debug=True)
