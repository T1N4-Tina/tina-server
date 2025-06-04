from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/comando', methods=['POST'])
def ricevi_comando():
    data = request.get_json()
    comando = data.get("comando", "")

    # Verifica formato: es. parla("Ciao")
    if not re.match(r'^\w+\(\".*\"\)$', comando):
        return jsonify({
            "stato": "errore",
            "messaggio": "Formato comando non valido: usa es. parla(\"testo\")"
        })

    try:
        with open("comando_corrente.txt", "w") as f:
            f.write(comando)

        return jsonify({
            "stato": "ok",
            "messaggio": f"Comando ricevuto e salvato: {comando}"
        })

    except Exception as e:
        return jsonify({
            "stato": "errore",
            "messaggio": f"Errore salvataggio comando: {str(e)}"
        })

@app.route('/', methods=['GET'])
def home():
    return "Tina è viva 🧠🤖"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
