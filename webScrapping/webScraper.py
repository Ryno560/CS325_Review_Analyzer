import requests
from bs4 import BeautifulSoup

class webScraper:
    def __init__(self, url):
        self.url = url
        self.page_content = None
        self.soup = None

    def fetch_page_content(self):
        #Fetches the HTML content of the page.
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.page_content = response.text
                self.soup = BeautifulSoup(self.page_content, 'html.parser')
            else:
                print(f"Failed to retrieve content. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_reviews(self, review_class):
        
        #Extracts reviews from the page using the provided CSS class name.
        #:param review_class: The class name of the HTML element containing the reviews.
        #:return: A list of reviews (as strings).

        if self.soup is None:
            print("Content not fetched. Call fetch_page_content() first.")
            return []

        reviews = []
        try:
            review_elements = self.soup.find_all(class_=review_class)
            reviews = [review.get_text(strip=True) for review in review_elements]
        except Exception as e:
            print(f"An error occurred while parsing reviews: {e}")

        return reviews

