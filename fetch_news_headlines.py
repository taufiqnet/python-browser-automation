import requests
from bs4 import BeautifulSoup
import time

def fetch_news_headlines():
    url = "https://www.thedailystar.net/news"

    # Send a GET request to the news website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    # Parse the content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all headline elements
    headlines = soup.find_all('h3')

    if not headlines:
        print("No headlines found.")
        return

    # Extract and print the text of each headline
    for index, headline in enumerate(headlines, start=1):
        print(f"{index}. {headline.get_text(strip=True)}")

    # Find the first article URL
    first_article = headlines[0].find('a')
    if first_article and 'href' in first_article.attrs:
        article_url = first_article['href']
        # Check if the URL is complete, otherwise append the base URL
        if not article_url.startswith('http'):
            article_url = "https://www.thedailystar.net" + article_url

        print(f"\nNavigating to the first article: {article_url}")

        # Send a GET request to the first article's URL
        article_response = requests.get(article_url)

        if article_response.status_code != 200:
            print(f"Failed to retrieve the article. Status code: {article_response.status_code}")
            return

        # Parse the content of the article page
        article_soup = BeautifulSoup(article_response.content, "html.parser")

        # Find the title of the article
        article_title = article_soup.find('h1', class_='fw-700 e-mb-16 article-title')
        if article_title:
            print(f"\nArticle Title: {article_title.get_text(strip=True)}")

        # Find the subtitle of the article
        article_subtitle = article_soup.find('div', class_='bg-cyan br-4 e-p-12 e-mb-16 text-16')
        if article_subtitle:
            print(f"Article Subtitle: {article_subtitle.get_text(strip=True)}")

        # Find the main content of the article
        article_content = article_soup.find('div', class_='pb-20 clearfix')
        if article_content:
            paragraphs = article_content.find_all('p')
            article_text = "\n".join([para.get_text(strip=True) for para in paragraphs])

            print("\nReading the article for 10 seconds...")
            time.sleep(10)  # Simulate reading the article for 10 seconds

            print("\nArticle has been read. Here is the content:")
            print(article_text[:1000])  # Print the first 500 characters of the article as a preview
        else:
            print("Could not find the article content.")
    else:
        print("No valid first article URL found.")

if __name__ == "__main__":
    fetch_news_headlines()
