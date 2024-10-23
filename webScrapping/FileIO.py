#Author: Ryan Hanks
#File: FileIO.py
#Description: This file does nothing when executed. 
#The File class is created with constructor that accepts both an input and output file as arguments
#Also declared are the member functions read and write 

class File:

    # read function reads lines from the given input file one by one and stores them into a list
    def read(self, input_file: str) -> list:
        # Reads from the input file.
        try:
            with open(input_file, "r") as file:
                lines = file.readlines()
                return [line.strip() for line in lines]
        except FileNotFoundError:
            print(f"Error: {input_file} not found.")
            return []

    # write function appends the given response string to the given output file
    def write(self, output_file: str, response: str):
        # Writes the response string to the output file.
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(response + "\n")