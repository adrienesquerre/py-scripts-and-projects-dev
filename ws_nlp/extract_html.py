import requests
from bs4 import BeautifulSoup
# from requests.auth import HTTPBasicAuth

# Disable InsecureRequestWarning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_html(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # This will raise an error for bad requests
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    url = "https://en.wikipedia.org/wiki/List_of_military_aid_to_Ukraine_during_the_Russo-Ukrainian_War"
    html_content = get_html(url)

    if html_content:
        # Optionally, save the HTML to a file for easier inspection
        with open("wikipedia_page.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        print("HTML content fetched and saved.")
    else:
        print("Failed to retrieve HTML content.")

if __name__ == "__main__":
    main()
