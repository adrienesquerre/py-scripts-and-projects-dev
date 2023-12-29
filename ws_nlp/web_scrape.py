from bs4 import BeautifulSoup
import requests
import json
# from requests.auth import HTTPBasicAuth

# Disable InsecureRequestWarning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extract_military_items(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []

    for p_tag in soup.find_all('p'):
        if p_tag.b:
            category = p_tag.b.text
            ul_tag = p_tag.find_next_sibling('ul')
            if ul_tag:
                for li_tag in ul_tag.find_all('li'):
                    item = {
                        'category': category,
                        'description': li_tag.get_text().strip(),
                        'link': li_tag.a['href'] if li_tag.a else None
                    }
                    data.append(item)
    return data

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# URL to scrape
url = 'https://en.wikipedia.org/wiki/List_of_military_aid_to_Ukraine_during_the_Russo-Ukrainian_War'
military_data = extract_military_items(url)
save_to_json(military_data, 'extracted_military_data.json')
