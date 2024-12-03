# Author: Ryan Hanks
# File: Main.py
# Description: This script reads URLs from a text file, 
# scrapes reviews, uses an AI model to classify them, and writes results to output files.

from webScraper import webScraper
from AI import AI
from FileIO import File
import matplotlib.pyplot as plt
from collections import Counter

def process_reviews():
    # Initialize the File, AI, and setup paths
    file_io = File()
    ai = AI()
    links_file = "links.txt"
    review_class_name = "fdbk-container__details__comment"  # Update with the correct CSS class name for reviews

    # Read URLs from links.txt
    urls = file_io.read(links_file)
    if not urls:
        print("No URLs found in links.txt")
        return [], []  # Return empty lists if no URLs

    output_files = []  # Initialize the list to hold output files

    # Process each URL
    for index, url in enumerate(urls, start=1):
        print(f"Processing URL {index}/{len(urls)}: {url}")
        
        # Scrape reviews
        scraper = webScraper(url)
        scraper.fetch_page_content()
        reviews = scraper.get_reviews(review_class_name)

        # If no reviews are found, skip the URL
        if not reviews:
            print(f"No reviews found for URL: {url}")
            continue

        # Generate output file name
        output_file = f"output_{index}.txt"
        output_files.append(output_file)  # Append output file name to the list

        # Classify each review and write to the output file
        for review in reviews:
            response = ai.getResponse(f"Classify this review as positive, negative, or neutral. Respond with only one word: {review}").lower()
            file_io.write(output_file, response)

        print(f"Results written to {output_file}")

    return urls, output_files  # Return URLs and output files for plotting

def plot_sentiment_counts(output_files):
    sentiment_counts = Counter()

    # Read each output file and count sentiments
    for file in output_files:
        try:
            with open(file, 'r') as f:
                sentiments = [line.strip() for line in f.readlines()]
                sentiment_counts.update(sentiments)
        except FileNotFoundError:
            print(f"File {file} not found.")
            continue

    # Extract labels and counts
    labels = ['positive', 'negative', 'neutral']
    counts = [sentiment_counts[label] for label in labels]

    # Plot bar chart
    plt.bar(labels, counts, color=['green', 'red', 'blue'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiments')
    plt.ylabel('Counts')
    plt.show()

if __name__ == "__main__":
    urls, output_files = process_reviews()  # Get URLs and output files
    if urls:  # Only plot if there are reviews processed
        plot_sentiment_counts(output_files)
