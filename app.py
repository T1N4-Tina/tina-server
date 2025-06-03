from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    # Simulazione: oggetti rilevati nell'immagine
    response = {
        "status": "ok",
        "oggetti": [
            {"nome": "Tavolo", "centroide": {"x": 320, "y": 400}},
            {"nome": "Sedia", "centroide": {"x": 480, "y": 420}},
            {"nome": "Bicchiere", "centroide": {"x": 510, "y": 350}}
        ],
        "json_file_url": "https://example.com/files/oggetti.json"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)