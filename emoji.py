from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_random_emoji():
    category = request.args.get('category')  # Kategori parametresini al

    url = 'https://emojihub.yurace.pro/api/random'

    if category:
        url += f'?category={category}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Doğru veri yapısını kontrol et
        if 'name' in data and 'category' in data and 'group' in data and 'htmlCode' in data and 'unicode' in data:
            return jsonify(data)
        else:
            return jsonify({"error": "Beklenen veri yapısı bulunamadı."})
    else:
        return jsonify({"error": "Bir hata oluştu.", "status_code": response.status_code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

