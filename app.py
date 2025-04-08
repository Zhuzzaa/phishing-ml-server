from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import extract_features_from_url
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Загружаем модель
model = joblib.load("phishing_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    urls = data.get("features", [])

    results = []
    for url in urls:
        features = extract_features_from_url(url)
        prediction = model.predict([features])[0]
        results.append(int(prediction))

    return jsonify({"result": results[0] if len(results) == 1 else results})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
