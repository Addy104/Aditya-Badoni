from flask import Flask, request, jsonify
from flask_cors import CORS
from checksum import compute_checksum, simulate_transmission

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    content = file.read().decode('utf-8')
    error_rate = float(request.form.get('errorRate', 0.1))
    checksum = compute_checksum(content)
    results = simulate_transmission(content, error_rate)
    return jsonify({'checksum': checksum, 'transmission': results})

if __name__ == '__main__':
    app.run(debug=True)
