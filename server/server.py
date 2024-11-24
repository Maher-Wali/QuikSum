from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    # Get the input from the client
    data = request.get_json()
    user_input = data.get("input", "")
    print(f"Received input: {user_input}")

    try:
        # Use subprocess to call the external Python script
        result = subprocess.run(
            ["python", "inference.py"],            # Command to run the script
            input=json.dumps({"input",user_input}),                  # Pass the user input
            text=True,                         # Ensure input/output as text
            capture_output=True                # Capture stdout and stderr
        )

        # Log output and errors for debugging
        print(f"Script Output: {result.stdout.strip()}")
        print(f"Script Errors: {result.stderr.strip()}")

        # Check if the script ran successfully
        if result.returncode != 0:
            return jsonify({"error": f"Script failed with code {result.returncode}: {result.stderr.strip()}"}), 500

        # Send the script's output back to the client
        return jsonify({"result": result.stdout.strip()})

    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
