import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.data = []

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.extract_data(soup)
        else:
            print("Failed to retrieve data from the website.")

    def extract_data(self, soup):
        # Example: Scrape article titles and links from a blog
        articles = soup.find_all('article')
        for article in articles:
            # Try to find the title in different tags
            title_tag = article.find('h2') or article.find('h1') or article.find('h3')
            if title_tag:
                title = title_tag.text.strip()
                link = article.find('a')['href'] if article.find('a') else 'No link found'
                self.data.append({'title': title, 'link': link})
            else:
                print("No title found for this article.")

    def save_to_csv(self, filename):
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
        print(f"Data saved to {filename}")

if __name__ == "__main__":
    url = "https://example-blog.com"  # Replace with the target website
    scraper = WebScraper(url)
    
    scraper.fetch_data()

    # Save data in different formats
    scraper.save_to_csv('articles.csv')
    scraper.save_to_json('articles.json')
