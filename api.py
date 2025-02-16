from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",  # Change if hosted remotely
    user="root",       # Your MySQL username
    password="root", # Your MySQL password
    database="dynamicprice"
)
cursor = db.cursor(dictionary=True)

# API Endpoint to Fetch Data
@app.route("/api/data", methods=["GET"])
def get_data():
    try:
        cursor.execute("SELECT * FROM products")
        results = cursor.fetchall()
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start Server
if __name__ == "__main__":
    app.run(debug=True, port=3000)
