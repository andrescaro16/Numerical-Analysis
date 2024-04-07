from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/vtex-webhook', methods=['POST'])
def vtex_webhook():
    data = request.json
    print("Datos recibidos de VTEX:", data)
    # Aquí procesarías los datos y luego enviarías lo necesario a SendPulse
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)