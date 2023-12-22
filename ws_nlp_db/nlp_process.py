import json
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def process_text_with_nlp(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    processed_data = []
    for item in data:
        doc = nlp(item['description'])
        # Process the text and extract information
        # For example, finding specific entities or keywords
        # Update 'item' with new fields or processed information if necessary
        processed_data.append(item)

    return processed_data

def save_processed_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# File to process
filename = 'extracted_military_data.json'
processed_data = process_text_with_nlp(filename)
save_processed_data(processed_data, 'processed_military_data.json')
