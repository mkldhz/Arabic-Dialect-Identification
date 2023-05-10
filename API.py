from flask import Flask, request, jsonify

from DialectModel import DialectModel


app = Flask(__name__)



@app.route('/api/predict', methods = ['POST'])
def POST():
    data = request.get_json()
    text = data['text']
    model_chosen = data['model_chosen']
    if model_chosen == 'Naive Bayes':
        prediction = M.predict_NB(text)
    elif model_chosen == 'LSTM':
        prediction = M.predict_LSTM(text)
    
    response = {'prediction': prediction}
    return jsonify(response)



if __name__ == '__main__':
    M = DialectModel()
    app.run(debug=True)