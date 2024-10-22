#Author: Ryan Hanks
#File: FileIO.py
#Description: This file does nothing when executed. 
#The File class is created with constructor that accepts both an input and output file as arguments
#Also declared are the member functions read and write 

class File:

    #File class constructor accepts an input file string and an output file string
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    #read member function reads lines from the input file one by one and stores them into a list
    def read(self) -> str:
    #Reads from the input file.
        try:
            with open(self.input_file, "r") as file:
                lines = file.readlines()
                return [line.strip() for line in lines]
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
            return ""
        
    #write member function appends the given response string to the output file
    def write(self, response: str):
    #Writes the response string to the output file.
        with open(self.output_file, "a") as file:
            file.write(response + "\n")