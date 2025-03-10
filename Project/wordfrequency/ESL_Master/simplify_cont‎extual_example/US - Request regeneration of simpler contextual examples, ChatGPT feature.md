## Name
Project feature:
As an ESL learner, if I feel that I have not adequately captured the meaning of a word in the original sentence context, I want the option to request the system to regenerate a particular example using simpler language and familiar vocabulary, so that I can better understand the usage of the word in the context.

## Description
This project is a Flask application that utilizes the OpenAI API to rewrite sentences using simpler vocabulary. The purpose is to generate a new sentence based on user input, containing a specific word, but using simpler language.

Acceptance Criteria:
The user should be able to self-assess their understanding of the contextual examples provided by the system.


If the user feels they have not adequately understood the original example, the system must offer the option to request a regenerated example using simpler language.


Regenerated examples should maintain the context and meaning of the original examples while using simpler language, sentence structures, and familiar vocabulary.


The system must generate and display regenerated examples within 10 seconds.


The user interface must include a clear and intuitive way to request regenerated examples (e.g., a button or toggle switch).


The system should update the user's scores and recalculate the learning metrics based on the regenerated examples.

## Installation
# Configuration design
To keep the API key secure and avoid exposing it in the code, we use the following configuration design:

1. Create a `.env` file in the project's root directory, and add the API key in the following format: API_KEY=your_openai_api_key_here

2. Add `.env` to the `.gitignore` file to ensure it is not tracked by Git and accidentally pushed to the repository.

3. Install the `python-dotenv` library if you haven't already:

```bash
pip install python-dotenv
```
4. In your Python code, use the following snippet to load the .env file and access the API key and your IP address:

```
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("API_KEY")
ip_address = os.environ.get("IP_ADDRESS")
```

By following these steps, the API key will be securely stored in the .env file, which will not be included in the Git repository.

Start the Flask server:

Run the following command in your terminal:

python <filename>.py
The server will start running on http://<your_ip_address>:5000.
Make a POST request to the /simplify_toggle endpoint with the following parameters:

input: The sentence you want to simplify.
word: The word that must be present in the new sentence.
Example request using cURL:

curl -X POST -d "input=This is a sample sentence.&word=sample" http://<your_ip_address>:5000/simplify_toggle

The server will use the OpenAI API to generate a new sentence based on the input and word. The response will be a JSON object containing the new sentence.


## Contributing


## Authors and acknowledgment
Laura Bedoyan
Rachel Gilyard
Rinali Kapadia 
Sushmitha K
Manpreet Dhindsa
Christian-John Vega 
Kranthi Setty
Comp 680 and 583 students

## License
Copyright (C) 2023  California State University Northridge COMP 680 Placeholdr 1 group

