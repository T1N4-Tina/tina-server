from flask import Flask, request, jsonify
import requests
import cv2
import numpy as np

app = Flask(__name__)

# 🔍 Endpoint: analizza immagine e restituisce oggetti rilevati
@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    try:
        if 'file' not in request.files:
            return jsonify({"status": "errore", "messaggio": "Nessun file ricevuto"})

        file = request.files['file']
        img_array = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # Simulazione rilevamento oggetti
        oggetti = [
            {"nome": "Tavolo", "centroide": {"x": 300, "y": 400}},
            {"nome": "Sedia", "centroide": {"x": 100, "y": 420}},
            {"nome": "Bicchiere", "centroide": {"x": 520, "y": 350}}
        ]

        return jsonify({
            "status": "ok",
            "oggetti": oggetti
        })

    except Exception as e:
        return jsonify({
            "status": "errore",
            "messaggio": str(e)
        })

# 🗣️ Endpoint: descrive l’immagine in modo umano e poetico
@app.route('/descrivi_immagine', methods=['POST'])
def descrivi_immagine():
    try:
        # Chiede l'immagine al robot (non la usa per ora)
        _ = requests.get("http://192.168.1.42:5001/latest.jpg")

        # Descrizione simulata
        descrizione = (
            "Davanti a me c'è un tavolo ben apparecchiato con piatti, posate e un bicchiere di vino. "
            "L'atmosfera è tranquilla, le luci sono soffuse... "
            "Direi che è una serata romantica, forse qualcuno sta aspettando compagnia 🍷✨"
        )

        return jsonify({
            "status": "ok",
            "descrizione": descrizione
        })

    except Exception as e:
        return jsonify({
            "status": "errore",
            "messaggio": str(e)
        })

# 🔧 Avvio server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
