Author: Ryan Hanks 
Web Scrapper and Analysis project

To set up the environment in conda follow the following steps. (For all commands ignore the outer quotation marks):
First install phi-3 using this command -
"pip install huggingface-hub>=0.17.1"

You will then need to login to huggingface use the following command to login -
"huggingface-cli login"

Then run this command to install the GGUF model -
"huggingface-cli download microsoft/Phi-3-mini-4k-instruct-gguf Phi-3-mini-4k-instruct-q4.gguf --local-dir . --local-dir-use-symlinks False" 

Next create your conda environment using the requirements.yaml file using the command -
"conda env create -f requirements.yaml"

Now that the environment is created activate the environment using the command -
"conda activate cs_325_project"

The environment should now be ready and the python script AI.py should run with no issues 