import joblib
from flask import Flask, request, json, jsonify, render_template

MODEL_PATH = "model/model.joblib"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.json:
        json_input = request.get_json()
        model = joblib.load(MODEL_PATH)
        prediction = model.predict (json_input["input"])
        prediction = float(prediction[0])
        response = { "prediction": prediction
        }
        return jsonify (response), 200
    return jsonify ({"msg": "Error, no JSON detected"})

if __name__ == "__main__":
    app.run(debug=True)
