import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            quotes = soup.find_all('div', class_='quote')

            print("\nExtracted Data:\n")
            for quote in quotes:
                text = quote.find('span', class_='text').get_text()
                author = quote.find('small', class_='author').get_text()
                print(f"{text} — {author}")
        else:
            print(f"Failed to retrieve page. Status code: {response.status_code}")
    except Exception as e:
        print("An error occurred:", e)

scrape_quotes("https://quotes.toscrape.com")
