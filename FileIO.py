class File:

    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    def read(self) -> str:
    #Reads from the input file.
        try:
            with open(self.input_file, "r") as file:
                lines = file.readlines()
                return [line.strip() for line in lines]
            return prompt
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
            return ""
        
    def write(self, response: str):
    #Writes the model response to the output file.
        with open(self.output_file, "a") as file:
            file.write(response + "\n")