from FileIO import File
from AI import AI

ai = AI()
file = File("input.txt", "output.txt")

prompts = file.read()

for prompt in prompts:
    file.write(ai.getResponse(prompt))