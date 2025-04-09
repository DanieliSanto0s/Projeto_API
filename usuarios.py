from flask import request, jsonify
from sqlalchemy import text
import database

db_connect = database.get_db_connection()

def get():
    try:
        conn = db_connect.connect()
        result = conn.execute(text('SELECT * FROM usuarios ORDER BY id'))
        data = [dict(zip(result.keys(), row)) for row in result]
        conn.close()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def getBy(id):
    try:
        conn = db_connect.connect()
        result = conn.execute(text('SELECT * FROM usuarios WHERE id = :id'), {"id": id})
        data = [dict(zip(result.keys(), row)) for row in result]
        conn.close()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def post():
    try:
        data = request.json
        nome = data.get('nome')
        email = data.get('email')
        password = data.get('password')

        conn = db_connect.connect()
        conn.execute(
            text("INSERT INTO usuarios (nome, email, password) VALUES (:nome, :email, :password)"),
            {"nome": nome, "email": email, "password": password}
        )
        conn.commit()

        result = conn.execute(text('SELECT * FROM usuarios ORDER BY id DESC LIMIT 1'))
        data = [dict(zip(result.keys(), row)) for row in result]
        conn.close()
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def alterar(id):
    try:
        data = request.json
        nome = data.get('nome')
        email = data.get('email')
        password = data.get('password')

        with db_connect.connect() as conn:
            conn.execute(
                text("UPDATE usuarios SET nome = :nome, email = :email, password = :password WHERE id = :id"),
                {"nome": nome, "email": email, "password": password, "id": id}
            )
            result = conn.execute(text('SELECT * FROM usuarios WHERE id = :id'), {"id": id})
            data = [dict(zip(result.keys(), row)) for row in result]

        return jsonify(data), 203
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def apagar(id):
    try:
        conn = db_connect.connect()
        conn.execute(text("DELETE FROM usuarios WHERE id = :id"), {"id": id})
        conn.commit()
        conn.close()
        return jsonify({"message": "Registro apagado com sucesso!"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def auth():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        conn = db_connect.connect()
        result = conn.execute(
            text('SELECT * FROM usuarios WHERE email = :email AND password = :password'),
            {"email": email, "password": password}
        )
        data = [dict(zip(result.keys(), row)) for row in result]
        conn.close()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
