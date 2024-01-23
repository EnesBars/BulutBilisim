from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/random_anime_quote', methods=['GET'])
def get_random_anime_quote():
    title = request.args.get('title')  # Başlık parametresini al
    name = request.args.get('name')    # Karakter adı parametresini al

    if title:
        url = f'https://animechan.xyz/api/random/anime?title={title}'
    elif name:
        url = f'https://animechan.xyz/api/random/character?name={name}'
    else:
        url = 'https://animechan.xyz/api/random'

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('anime') and data.get('character') and data.get('quote'):
            return jsonify(data)
        else:
            return jsonify({"error": "Veri formati uygun değil."})
    else:
        return jsonify({"error": "Bir hata oluştu.", "status_code": response.status_code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
