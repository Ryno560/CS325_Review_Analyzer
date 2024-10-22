#Author: Ryan Hanks
#File: AI.py
#Description: This file does nothing when executed. 
#The AI class is created with constructor that has no arguments that should be passed by the user
#Has a declared member function getResponse that returns a string

from llama_cpp import Llama

class AI:
    #constructot declares llm which is the variable used to access the phi3 model
    def __init__(self):

        self.llm = Llama(
        model_path="./Phi-3-mini-4k-instruct-q4.gguf",  # path to GGUF file
        n_ctx=4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
        n_threads=8, # The number of CPU threads to use, tailor to your system and the resulting performance
        n_gpu_layers=35, # The number of layers to offload to GPU, if you have GPU acceleration available. Set to 0 if no GPU acceleration is available on your system.
        )
    
    #returns the response of the phi3 model to an input string. The returned statement is also a string type 
    def getResponse(self, input: str) -> str:
         
        output = self.llm(
        f"<|user|>\n{input}\n<|assistant|>",
        max_tokens=256,  # Generate up to 256 tokens
        stop=["<|end|>"], 
        echo=True,  # Whether to echo the prompt
        )
         
        return output['choices'][0]['text']