from flask import Flask, jsonify, request
from datetime import datetime
from config import create_app
from classifier import get_sentiment, predict_sentiment

app = create_app()


@app.route('/time', methods=['GET'])
def get_current_time():
    return {'time': datetime.now().strftime("%m/%d/%Y %H:%M:%S")}

# create a POST route to use the get_sentiment function
@app.route('/sentiment', methods=['POST'])
def sentiment():
    # Get the input data
    data = request.get_json()
    text = data['text']

    # Get the sentiment of the inputted text
    # print(get_sentiment(text))

    return get_sentiment(text)


# create a POST route to get the input text
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data
    data = request.get_json()
    text = data['text']

    # Get the sentiment of the inputted text
    # print(predict_sentiment(text))

    return predict_sentiment(text)



if __name__ == '__main__':
    app.run(debug=True)