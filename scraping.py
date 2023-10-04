import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape quotes and authors from a given URL
def scrape_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []
    authors = []

    for quote in soup.find_all('span', class_='text'):
        quotes.append(quote.get_text())

    for author in soup.find_all('span', class_='small'):
        authors.append(author.find('span', class_='author').get_text())

    return quotes, authors

# Function to save quotes and authors to a CSV file
def save_to_csv(quotes, authors):
    with open('quotes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author'])
        for q, a in zip(quotes, authors):
            writer.writerow([q, a])

# Main function
def main():
    base_url = 'http://quotes.toscrape.com/page/'
    num_pages = 5  # Number of pages to scrape

    all_quotes = []
    all_authors = []

    for page_num in range(1, num_pages + 1):
        url = base_url + str(page_num)
        quotes, authors = scrape_quotes(url)
        all_quotes.extend(quotes)
        all_authors.extend(authors)

    save_to_csv(all_quotes, all_authors)
    print(f'Scraped {len(all_quotes)} quotes and authors. Saved to quotes.csv.')

if __name__ == '__main__':
    main()
