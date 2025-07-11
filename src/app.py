from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='password',
            database='prueba'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hola desde la base de datos MySQL!'")
        result = cursor.fetchone()
        return f'<h1>{result[0]}</h1>'
    except Exception as e:
        return f'<h1>Error de conexión a MySQL: {str(e)}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
