Web Scraper and Sentiment Analysis Project  
Author: Ryan Hanks  

Overview: 
This project scrapes reviews from websites, classifies them as positive, negative, or neutral using an AI model, and visualizes the results.

Features:  
- Scrapes reviews from URLs in `links.txt`.  
- Classifies reviews and outputs results in `GooglePixel_5.txt` to `GooglePixel_8.txt`.  
- Generates a grouped bar chart for sentiment analysis.  

Structure:
- Main.py: Orchestrates the process.  
- FileIO.py: Handles file I/O.  
- webScraper.py: Extracts reviews using BeautifulSoup.  
- AI.py: Classifies sentiment using an AI model.

Setup:  

Step 1: Install Dependencies  
1. First, install `huggingface-hub` (for accessing the AI model):  
   ```bash
   pip install huggingface-hub>=0.17.1
2. Log in to Hugging Face:
   ```bash
   huggingface-cli login
3. Download the Phi-3 model:
   ```bash
   huggingface-cli download microsoft/Phi-3-mini-4k-instruct-gguf Phi-3-mini-4k-instruct-q4.gguf --local-dir . --local-dir-use-symlinks False

Step 2: Setup Conda Environment
1. Download the requirements.yaml file
2. Create the Conda environment from the requirements.yaml file:
   ```bash
   conda env create -f requirements.yaml
3. Activate the environment:
   ```bash
   conda activate cs_325_project

Step 3: Prepare Files
1. Add your target URLs to links.txt.
2. If re-running the program, you may want to delete GooglePixel_5.txt through GooglePixel_8.txt from previous runs.

Step 4: Run the Program
1. Execute the following command to run the script:
   ```bash
   python Main.py
2. The script will produce the output files: GooglePixel_5.txt to GooglePixel_8.txt 
   and a bar chart showing sentiment distribution.



