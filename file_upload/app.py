from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Folder to save incoming data
if not os.path.exists("received_data"):
    os.makedirs("received_data")

@app.route("/")
def home():
    return "Local WiFi server is running 🚀"

# Endpoint to receive data (POST request)
@app.route("/send", methods=["POST"])
def receive_data():
    try:
        data = request.get_json()  # Expecting JSON from device
        if not data:
            return jsonify({"status": "error", "message": "No JSON received"}), 400

        # Save data into a file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"received_data/data_{timestamp}.json"

        with open(filename, "w") as f:
            f.write(str(data))

        return jsonify({"status": "success", "message": "Data received"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # Run on local WiFi
    app.run(host="0.0.0.0", port=5000, debug=True)
