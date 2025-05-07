from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configura conexión a la DB
def get_db():
    return mysql.connector.connect(
        host="db", user="root", password="123", database="miapp"
    )

@app.route('/api/registro', methods=['POST'])
def registro():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, usuario, password) VALUES (%s, %s, %s)",
                   (data['nombre'], data['usuario'], data['password']))
    conn.commit()
    return jsonify({"msg": "Cliente registrado"})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE usuario=%s AND password=%s",
                   (data['usuario'], data['password']))
    result = cursor.fetchone()
    if result:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return jsonify({"clientes": clientes})
    return jsonify({"msg": "Credenciales incorrectas"}), 401

@app.route('/api/productos', methods=['GET'])
def productos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return jsonify({"productos": productos})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
