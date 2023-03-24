# import AutoTokenizer to parse imputted tweets 
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from flask import Flask, jsonify, request
import torch

# Let's grab the model we want: cardiffnlp/twitter-xlm-roberta-base-sentiment
model_nm = 'cardiffnlp/twitter-xlm-roberta-base-sentiment'

tokenizer = AutoTokenizer.from_pretrained(model_nm)
model = AutoModelForSequenceClassification.from_pretrained(model_nm)
device = torch.device('cpu')  # or 'cuda' if you're using a GPU
model.to(device)
model.eval()

def predict_sentiment(input_text):
    # Tokenize the input text and convert to tensor
    inputs = tokenizer(input_text, padding=True, truncation=True, return_tensors='pt').to(device)

    # Make a prediction using the model
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits, dim=1)

    # Return the predicted class as a JSON response
    return jsonify({'class': predicted_class.item()})



tokz = AutoTokenizer.from_pretrained(model_nm)

# Load the tokenizer and model
model = AutoModelForSequenceClassification.from_pretrained(model_nm)

# Create a text classification pipeline
classifier = pipeline('text-classification', model=model, tokenizer=tokz)

def get_sentiment(input_text):
    # Get the sentiment of the inputted text
    sentiment = classifier(input_text)[0]
    return sentiment
    
