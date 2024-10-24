#Author: Ryan Hanks
#File: Main.py
#Description: This file reads in the links from the file links.txt, 
#and scrapes the reviews from each link given and stores each link's reviews into seperate txt files 

#imports the two classes for web scrapping use and FileIO use
from FileIO import File
from webScraper import webScraper

#declares the file variable which will be used for file input and output purposes
file = File()

#declares the urls variable which is a list of the urls read in from the links.txt file
urls = file.read("links.txt")

#declares the pixel_num variable which is an integer that keeps track of the version of the phone for output file name
pixel_num = 9

#for loop that runs for each url in the urls list
for url in urls:
    #creates the name of the output file and then decrements pixel_num because the urls are in the order 9 8 7 6
    output_file = "google_pixel_" + str(pixel_num) + "_reviews.txt"
    pixel_num -= 1

    #declares the name of the class in the html code of the website where the reviews are located
    review_class = "fdbk-container__details__comment"

    #declares a variable scraper of the webScraper class and provides the url for the constructor
    scraper = webScraper(url)
    #fetches the HTML content from the given URL
    scraper.fetch_page_content()
    #gets the reviews from the HTML content and stores them into the reviews list
    reviews = scraper.get_reviews(review_class)

    #for loop to write each review from the reviews list to the output file
    for idx, review in enumerate(reviews, 1):
        file.write(output_file ,f"Review {idx}: {review}")