from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/start-luna', methods=['POST'])
def start_luna():
    """Endpoint to start LUNA Assist when mic is clicked."""
    try:
        subprocess.Popen(["python", "main.py"])  # Runs main.py in a separate process
        return jsonify({"message": "LUNA Assist started!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
