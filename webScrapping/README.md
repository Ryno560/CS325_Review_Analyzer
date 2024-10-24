Author: Ryan Hanks 
Web Scrapper and Analysis project

This software (Main.py) reads in links from a text file (links.txt) and then extracts the reviews from the website
The software then outputs the extracted data into seperate text files for each link.
The software uses 2 packages beautifulsoup4 and requests to scrape the data from the website, Ebay in this case.
There is also 2 classes used in main I created one for File input and output and the other to scrape the data from the webpage.

SETUP:

To create your conda environment first download the requirements.yaml file and then use the command -
"conda env create -f requirements.yaml"

Now that the environment is created activate the environment using the command -
"conda activate cs_325_webScrapping"

The environment should now be ready and the python script Main.py should run with no issues as long as links.txt is downloaded
However the output files that are in git are already full so you may want to delete google_pixel_#_reviews.txt
replace the # symbol with 6, 7, 8, and 9 to delete all output files.

To run Main.py use the command -
"python Main.py"

This will produce the four output files mentioned above.

The other scripts included are FileIO.py and webScraper.py which each include a class that are used by Main.py 
but do nothing on their own