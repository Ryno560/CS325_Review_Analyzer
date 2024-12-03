# Author: Ryan Hanks
# File: Main.py
# Description: This script automates the process of scraping reviews from websites,
# classifies the sentiment of each review using an AI model, and visualizes the results.

from webScraper import webScraper
from AI import AI
from FileIO import File
import matplotlib.pyplot as plt
from collections import Counter


def process_reviews():
    """
    Reads URLs from a text file, scrapes reviews from each URL, classifies each review's sentiment, 
    and writes the results to separate output files. Returns the list of processed URLs and output files.

    Returns:
        tuple: A tuple containing:
            - urls (list): List of URLs processed.
            - output_files (list): List of output file names.
    """
    # Initialize helper classes
    file_io = File()
    ai = AI()

    # Path to the file containing URLs
    links_file = "links.txt"

    # CSS class name of the HTML elements containing the reviews
    review_class_name = "fdbk-container__details__comment"

    # Read URLs from the file
    urls = file_io.read(links_file)
    if not urls:
        print("No URLs found in links.txt")
        return [], []  # Return empty lists if no URLs are provided

    # List to store names of output files
    output_files = []

    # Process each URL
    for index, url in enumerate(urls, start=5):  # File names start from GooglePixel_5
        print(f"Processing URL {index}/{len(urls)}: {url}")

        # Create a webScraper instance for the current URL
        scraper = webScraper(url)
        scraper.fetch_page_content()  # Fetch the page's HTML content
        reviews = scraper.get_reviews(review_class_name)  # Extract reviews using the CSS class

        # Skip URLs with no reviews
        if not reviews:
            print(f"No reviews found for URL: {url}")
            continue

        # Generate output file name based on the URL index
        output_file = f"GooglePixel_{index}.txt"
        output_files.append(output_file)

        # Classify each review and write the sentiment to the output file
        for review in reviews:
            prompt = f"Classify this review as positive, negative, or neutral. Respond with only one word: {review}"
            response = ai.getResponse(prompt).lower()  # Get AI response and convert to lowercase
            file_io.write(output_file, response)  # Write the response to the output file

        print(f"Results written to {output_file}")

    return urls, output_files


def plot_sentiment_counts(output_files):
    """
    Reads the sentiment classifications from the output files and visualizes the distribution of sentiments
    (positive, negative, neutral) for each file using a grouped bar chart.

    Args:
        output_files (list): List of output file names containing sentiment classifications.
    """
    import numpy as np

    # List to store sentiment counts for each output file
    sentiment_counts_per_file = []

    # Read each output file and count sentiments
    for file in output_files:
        sentiment_counts = Counter()
        try:
            # Read sentiment classifications from the file
            with open(file, 'r') as f:
                sentiments = [line.strip() for line in f.readlines()]
                sentiment_counts.update(sentiments)
        except FileNotFoundError:
            print(f"File {file} not found.")
            sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}  # Default counts

        sentiment_counts_per_file.append(sentiment_counts)

    # Extract sentiment labels
    labels = ['positive', 'negative', 'neutral']
    n_files = len(output_files)

    # Bar chart configuration
    x = np.arange(n_files)  # Positions for each output file group
    width = 0.2  # Width of each bar

    # Initialize plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot grouped bars for each sentiment
    for i, label in enumerate(labels):
        # Get counts for the current sentiment across all files
        counts = [file_counts.get(label, 0) for file_counts in sentiment_counts_per_file]
        ax.bar(x + i * width, counts, width, label=label)  # Plot the bar group

    # Set x-axis labels to file names (e.g., GooglePixel_5, GooglePixel_6)
    file_names = [f"GooglePixel_{i+5}" for i in range(n_files)]
    ax.set_xticks(x + width)  # Center the groups
    ax.set_xticklabels(file_names)

    # Add chart title and axis labels
    ax.set_title('Sentiment Distribution per Output File')
    ax.set_xlabel('Output Files')
    ax.set_ylabel('Counts')

    # Add legend for sentiment types
    ax.legend(title="Sentiments")

    # Display the chart
    plt.show()


if __name__ == "__main__":
    # Process reviews and retrieve URLs and output file names
    urls, output_files = process_reviews()

    # Plot the sentiment distribution if there are reviews
    if urls:
        plot_sentiment_counts(output_files)
