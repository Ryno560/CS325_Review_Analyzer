#Author: Ryan Hanks
#File: webScraper.py
#Description: Includes the class webScraper that uses the requests and beautifulsoup4 
#packages to scrape data from a given url.

import requests
from bs4 import BeautifulSoup

#class: webScraper
#Has contructor that has one argument, url, which is given by the user.
#fetch_page_content member function fetches all of the HTML content of the webpage.
#get_reviews cleans up the HTML retrieving all content from the provided 
#CSS class returning a list of each instance of the class (as strings).
class webScraper:
    #constructor has one argument url
    def __init__(self, url):
        self.url = url
        self.page_content = None
        self.soup = None

    #Fetches the HTML content of the page.
    def fetch_page_content(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.page_content = response.text
                self.soup = BeautifulSoup(self.page_content, 'html.parser')
            else:
                print(f"Failed to retrieve content. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

    #Extracts reviews from the page using the provided CSS class name.
    #The paramater is review_class: The class name of the HTML element containing the reviews.
    #Returns A list of reviews (as strings).
    def get_reviews(self, review_class):

        if self.soup is None:
            print("Content not fetched.")
            return []

        reviews = []
        try:
            review_elements = self.soup.find_all(class_=review_class)
            reviews = [review.get_text(strip=True) for review in review_elements]
        except Exception as e:
            print(f"An error occurred while parsing reviews: {e}")

        return reviews

