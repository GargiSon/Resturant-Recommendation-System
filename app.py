import os
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Ensure model exists
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
if not os.path.exists(model_path):
    raise FileNotFoundError("Error: model.pkl file not found. Train the model first.")

# Load model
try:
    model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    raise RuntimeError("Error loading model: " + str(e))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 1)
        return render_template('index.html', prediction_text='Your Rating is: {}'.format(output))
    except Exception as e:
        return render_template('index.html', prediction_text="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
