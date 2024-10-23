from FileIO import File
from webScraper import webScraper


file = File()

urls = file.read("links.txt")

pixel_num = 6

for url in urls:
    output_file = "google_pixel_" + str(pixel_num) + "_reviews.txt"
    pixel_num += 1

    review_class = "fdbk-container__details__comment"

    scraper = webScraper(url)
    scraper.fetch_page_content()
    reviews = scraper.get_reviews(review_class)

    for idx, review in enumerate(reviews, 1):
        file.write(output_file ,f"Review {idx}: {review}")