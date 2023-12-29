import json
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# List of specific military entities
military_entities = ["tank", "rifle", "grenade launcher", "machine gun", "artillery", "missile"]

def find_military_entities_with_context(text, entities):
    doc = nlp(text)
    found_entities_with_context = {}

    for sent in doc.sents:
        for token in sent:
            if token.text.lower() in entities:
                found_entities_with_context[token.text] = sent.text

    return found_entities_with_context

def process_text_with_nlp(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    processed_data = []
    for item in data:
        entities_context = find_military_entities_with_context(item['description'], military_entities)

        # Update the item with new fields or processed information
        item['military_entities'] = entities_context
        processed_data.append(item)

    return processed_data

def save_processed_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# File to process
filename = 'extracted_military_data.json'
processed_data = process_text_with_nlp(filename)
save_processed_data(processed_data, 'processed_military_data.json')
