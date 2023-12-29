from bs4 import BeautifulSoup
import json

def extract_military_items(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []

    # Find all paragraph tags, they might contain the category headings
    for p_tag in soup.find_all('p'):
        # Check if the paragraph tag contains a bold tag (likely a category heading)
        if p_tag.b:
            category = p_tag.b.text
            # The next sibling of the paragraph tag is likely the unordered list of items
            ul_tag = p_tag.find_next_sibling('ul')
            if ul_tag:
                for li_tag in ul_tag.find_all('li'):
                    item = {
                        'category': category,
                        'description': li_tag.get_text().strip(),
                        'link': li_tag.a['href'] if li_tag.a else None  # Get hyperlink if available
                    }
                    data.append(item)
    return data

# Read the HTML content from the file
with open('wikipedia_page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Call the function with the HTML content
military_data = extract_military_items(html_content)

# Save the extracted data to a JSON file
with open('extracted_military_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(military_data, json_file, indent=4, ensure_ascii=False)

print("Data extraction complete and saved to 'extracted_military_data.json'")
