import json

from flask import Flask, request
from sklearn.externals import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)


@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.data
    data_dict = json.loads(data)
    print(data_dict)
    power = predict_power([data_dict['param']])
    return json.dumps(str(power[0][0]))


def predict_power(param):
    model = load_model('DNN_2layer.h5')
    scalar_filename = "scaler.save"
    scalar = joblib.load(scalar_filename)
    return model.predict(scalar.transform(param))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
