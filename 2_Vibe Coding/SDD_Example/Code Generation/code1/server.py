from flask import Flask, request, jsonify, render_template
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    text = data.get("text")
    target_lang = data.get("target")

    if not text or not target_lang:
        return jsonify({"error": "Missing text or target language"}), 400

    # googletrans 4.0.0-rc1 is synchronous
    result = translator.translate(text, dest=target_lang)

    return jsonify({
        "source_text": text,
        "source_lang": result.src,
        "translated_text": result.text,
        "target_lang": target_lang
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
