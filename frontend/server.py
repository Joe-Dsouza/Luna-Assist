from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import subprocess
import time
import queue
import threading

app = Flask(__name__)
CORS(app)

# Queue to store live conversation output
text_queue = queue.Queue()

def read_luna_output():
    """Simulated function to get real-time output from LUNA Assist."""
    while True:
        # Replace this with actual logic to capture LUNA's response
        text_queue.put("LUNA: How can I assist you?")
        time.sleep(2)  # Simulating conversation delay

# Start a background thread to fetch responses from LUNA
threading.Thread(target=read_luna_output, daemon=True).start()

@app.route('/start-luna', methods=['POST'])
def start_luna():
    """Endpoint to start LUNA Assist when mic is clicked."""
    try:
        subprocess.Popen(["python", "main.py"])  # Runs main.py in a separate process
        return jsonify({"message": "LUNA Assist started!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stream')
def stream():
    """Server-Sent Events (SSE) endpoint to stream live conversation."""
    def event_stream():
        while True:
            if not text_queue.empty():
                text = text_queue.get()
                yield f"data: {text}\n\n"
            time.sleep(1)

    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
