#import libs
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os


app = Flask(__name__)

# Get the current directory
load_dotenv()
API_KEY = os.environ.get("API_KEY")
IP_ADDRESS = os.environ.get("IP_ADDRESS")

openai.api_key = API_KEY

@app.route('/simplify_toggle', methods=['POST'])
def generate_examples():
    """
    Generate simplified examples using OpenAI's language model.

    Returns:
        Flask Response: JSON response containing the generated examples.

    Description:
        This function handles the POST request to the '/simplify_toggle' endpoint.
        It retrieves the 'input' and 'word' parameters from the query parameters,
        checks if the 'input' parameter is missing, constructs a prompt for the OpenAI model,
        uses the OpenAI API to generate a response, and returns the response as a JSON object.
    """
    # Retrieve the 'input' and 'word' parameters from the query parameters
    user_input = request.args.get('input')
    user_word = request.args.get('word')
    
    # Check if 'input' parameter is missing
    if user_input is None:
        return jsonify({'error': 'Missing input parameter'}), 400
    
    # Construct the prompt for the OpenAI model
    # Construct the prompt for the OpenAI model
    prompt = (
        f"Can you re-write this sentence '{user_input}' using simpler vocabulary "
        f"and shorter than the original to be easier? "
        f" Your new output must be one sentence "
        f"and MUST contain the word '{user_word}'."
        )


    # Use OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the message content from the API response
    message_content = response['choices'][0]['message']['content']
    
    # Check if the conversion to JSON was successful
    if not message_content:
        return jsonify({'error': 'Invalid data format'}), 400

    # Convert the message content to JSON format
    json_array = jsonify(message_content)
 
    # Check if the conversion to JSON was successful
    if json_array is None:
        return jsonify({'error': 'Invalid data format'}), 400

    return json_array

#run main flask app
if __name__ == '__main__':
    """
    Run the Flask app.

    Returns:
        None

    Description:
        This block of code runs the Flask app when the script is directly executed.
        It sets the host and port, and enables debugging mode.
    """
    app.run(host=IP_ADDRESS, port=5000, debug=True)
