from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)


model_name = "google/flan-t5-base"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    inputs = tokenizer(text, return_tensors="pt")
    output_sequences = model.generate(
        input_ids=inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=50,  
        num_return_sequences=1,  
    )
    
    # Decode the generated text
    predicted_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)

    return jsonify({'predicted_text': predicted_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
