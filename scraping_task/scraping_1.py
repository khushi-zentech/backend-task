"""
Task - 30: Scrapping Project - 1. (BeautifulSoup)
Scrape quotes from https://quotes.toscrape.com this link.
"""

# import required BeautifulSoup library
import requests
from bs4 import BeautifulSoup

# define class of Scrap_Quotes to scrape quotes
class Scrape_Quotes:
    # constructor to intialize url and quotes list
    def __init__(self, url):
        self.url = url
        self.quotes = []

    # define function to scrape quotes from url
    def scrape_quotes(self):
        page = 1
    
        while True:
            page_url = f"{self.url}/page/{page}/"
            responses = requests.get(page_url)
            html_doc = responses.content
            
            soup = BeautifulSoup(html_doc, "html.parser")
    
            quote_blocks = soup.find_all("div", class_="quote")
    
            if not quote_blocks:
                break
    
            for q in quote_blocks:
                text = q.find("span", class_="text").text
                author = q.find("small", class_="author").text
                tags = [tag.text for tag in q.find_all("a", class_="tag")]
                
                author_link = q.find("a")["href"]
                author_details = self.url + author_link
    
                quote_data = {"Quote": text,"Author": author, "Tags": tags, "Author_Details": author_details}
                self.quotes.append(quote_data)
                
            page += 1

    # define function to display quote details
    def display_quotes(self):
        for i, q in enumerate(self.quotes):
            print("\nQuote No.     :", i+1)
            print("Quote         :", q["Quote"])
            print("Author        :", q["Author"])
            print("Author_Details:", q["Author_Details"])
            print("Tags          :", ", ".join(q["Tags"]))

# define function to create object 
def main():
    url = "https://quotes.toscrape.com"
    scrap_object = Scrape_Quotes(url)

    # call the method
    scrap_object.scrape_quotes()
    scrap_object.display_quotes()

# start from here
main()