from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configurations
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Kaushik@1234',
    'database': 'javatechie'
}

# Function to connect to MySQL
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(**mysql_config)
        return conn
    except mysql.connector.Error as err:
        print("Error: ", err)

# API endpoint to store entity in MySQL
@app.route('/api/entity', methods=['POST'])
def store_entity():
    try:
        conn = connect_to_mysql()
        cursor = conn.cursor()

        # Extract data from the request
        data = request.json
        id=data['id']
        name = data['name']
        description = data['description']

        # Insert data into MySQL
        insert_query = "INSERT INTO entities (id,name, description) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (id, name, description))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Entity stored successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/api/get', methods=['GET'])
def get_message():
    try:
      return jsonify({'message': 'sample welcome message from the API'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
