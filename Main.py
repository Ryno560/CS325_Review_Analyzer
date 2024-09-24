#Author: Ryan Hanks
#File: Main.py
#Description: This file reads in the lines from the file input.txt, 
#and gets a response to each question in input.txt from the phi3 AI model and puts the responses in output.txt

#imports the two classes for AI use and FileIO use
from FileIO import File
from AI import AI

#declares the ai variable that will be used to get a response from the phi3 model
ai = AI()
#declares the file variable which recieves input.txt and output.txt
file = File("input.txt", "output.txt")

#read the lines from the file and stores the list in prompts
prompts = file.read()

#for each string in the prompts list it sends the string to the ai module and outputs the response to the output file
for prompt in prompts:
    file.write(ai.getResponse(prompt))