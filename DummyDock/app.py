from flask import Flask, request, jsonify
import pickle
import os
from flasgger import Swagger
from fastapi import FastAPI

MODEL_DIR = 'models'
MODEL_NAME = 'tree'

app = Flask(__name__)
swagger = Swagger(app)

classifier = pickle.load(open(os.path.join(MODEL_DIR, MODEL_NAME + '.pkl'), 'rb'))


@app.route('/')
def welcome():
    return "Welcome to the Model Prediction API!"


@app.route('/predict', methods=['GET'])
def predict():
    """
    Predict the class based on input features.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        400:
            description: Invalid input parameters
    """
    try:
        variance = float(request.args.get('variance'))
        skewness = float(request.args.get('skewness'))
        curtosis = float(request.args.get('curtosis'))
        entropy = float(request.args.get('entropy'))

        prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
        return jsonify({"prediction": prediction.tolist()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)

