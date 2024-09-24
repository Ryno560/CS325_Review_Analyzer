#Author: Ryan Hanks
#File: Main.py
#Description: This file reads in the lines from the file input.txt, 
#and gets a response to each question in input.txt from the phi3 AI model and puts the responses in output.txt

from FileIO import File
from AI import AI

ai = AI()
file = File("input.txt", "output.txt")

prompts = file.read()

for prompt in prompts:
    file.write(ai.getResponse(prompt))