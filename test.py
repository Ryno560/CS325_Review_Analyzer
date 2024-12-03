from webScraper import webScraper
from AI import AI
from bs4 import BeautifulSoup

def test_web_scraper_fetch():
    url = "https://www.ebay.com/fdbk/mweb_profile?fdbkType=FeedbackReceivedAsSeller&item_id=276697390535&username=itsworthmore&filter=feedback_page%3ARECEIVED_AS_SELLER&sort=RELEVANCE"
    scraper = webScraper(url)
    scraper.fetch_page_content()
    assert scraper.page_content is not None
    assert scraper.soup is not None

def test_web_scraper_get_reviews():
    html_content = """
    <html><body>
    <div class="review">Good product</div>
    <div class="review">Bad service</div>
    </body></html>
    """
    scraper = webScraper("https://example.com")
    scraper.soup = BeautifulSoup(html_content, 'html.parser')
    reviews = scraper.get_reviews("review")
    assert reviews == ["Good product", "Bad service"]

def test_ai_response_positive():
    ai = AI()
    response = ai.getResponse("Classify this review as positive, negative, or neutral. Respond with only one word: Excellent product!")
    assert response == "positive"

def test_ai_response_negative():
    ai = AI()
    response = ai.getResponse("Classify this review as positive, negative, or neutral. Respond with only one word: Terrible experience.")
    assert response == "negative"
