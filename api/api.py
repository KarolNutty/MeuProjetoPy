from flask import Flask, request, jsonify
import sqlite3
import os
import atexit

app = Flask(__name__)

# Configuração do banco de dados
def cleanup_db():
    try:
        if os.path.exists('database.db'):
            os.remove('database.db')
    except Exception as e:
        print(f"Erro ao limpar banco de dados: {e}")

atexit.register(cleanup_db)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_operadoras_table():
    cleanup_db()  # Remove o banco de dados existente, se houver
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS operadoras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT NOT NULL UNIQUE,
            endereco TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Criação da tabela sempre que o app for inicializado
create_operadoras_table()

# Rota GET para listar operadoras
@app.route('/api/operadoras', methods=['GET'])
def get_operadoras():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM operadoras")
        operadoras = cursor.fetchall()
        conn.close()

        return jsonify([dict(operadora) for operadora in operadoras]), 200

    except Exception as e:
        print(f"Erro ao acessar banco de dados: {e}")
        return jsonify({"message": "Erro interno no servidor"}), 500


# Rota POST para adicionar operadora
@app.route('/api/operadoras', methods=['POST'])
def add_operadora():
    # Verificação robusta do JSON
    if not request.is_json:
        return jsonify({"message": "Requisição deve ser JSON"}), 400

    try:
        dados = request.get_json()
    except Exception:
        return jsonify({"message": "Requisição deve ser JSON"}), 400

    # Validação dos campos obrigatórios
    campos_obrigatorios = ['nome', 'cnpj', 'endereco', 'telefone']
    campos_faltantes = [campo for campo in campos_obrigatorios if campo not in dados]

    if campos_faltantes:
        return jsonify({
            "message": "Campos obrigatórios faltando",
            "missing_fields": campos_faltantes
        }), 400

    # Validação de valores não vazios
    campos_vazios = [campo for campo in campos_obrigatorios if not str(dados.get(campo, '')).strip()]
    if campos_vazios:
        return jsonify({
            "message": "Campos não podem ser vazios",
            "empty_fields": campos_vazios
        }), 400

    # Inserção no banco de dados
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(''' 
            INSERT INTO operadoras (nome, cnpj, endereco, telefone) 
            VALUES (?, ?, ?, ?) 
        ''', (
            dados['nome'].strip(),
            dados['cnpj'].strip(),
            dados['endereco'].strip(),
            dados['telefone'].strip()
        ))

        conn.commit()
        operadora_id = cursor.lastrowid
        conn.close()

        return jsonify({
            'id': operadora_id,
            'nome': dados['nome'],
            'cnpj': dados['cnpj'],
            'endereco': dados['endereco'],
            'telefone': dados['telefone']
        }), 201

    except sqlite3.IntegrityError as e:
        if "UNIQUE" in str(e):
            return jsonify({"message": "CNPJ já cadastrado"}), 409
        return jsonify({"message": "Dados inválidos para inserção"}), 400
    except Exception as e:
        print(f"Erro no banco de dados: {e}")
        return jsonify({"message": "Erro ao processar a requisição"}), 500

if __name__ == "__main__":
    app.run(debug=True)

