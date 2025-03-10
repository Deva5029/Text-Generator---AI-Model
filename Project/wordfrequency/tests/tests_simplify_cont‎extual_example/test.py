import requests
from dotenv import load_dotenv
import pytest
import requests
import os
import textstat

load_dotenv()
IP_ADDRESS = os.environ.get("IP_ADDRESS")

def test_my_api_endpoint():
    """
    Test the 'simplify_toggle' API endpoint.

    Returns:
        None

    Description:
        This function sends a POST request to the API endpoint with predefined data. 
        It validates the response status code, checks if the specified word is present 
        in the response, and prints the simplified sentence.
    """
    # Set up the necessary data for the request
    url = f"http://{IP_ADDRESS}:5000/simplify_toggle"
    word = "myths"
    input_data = (
    "These misconceptions often stay from outdated information or "
    "myths that have been perpetuated over time."
    )

    # Set the query parameters
    params = {
        "word": word,
        "input": input_data
    }

    # Send a POST request to the API endpoint
    response = requests.post(url, params=params)

    # Validate the response
    assert response.status_code == 200

    # Extract the response data
    data = response.text

    # Check if the word is present in the response (case-insensitive)
    assert word.lower() in data.lower()

    # Print the simplified sentence
    print("Response:", data)


def test_missing_word_parameter():
    """
    Test the case when the 'word' parameter is missing.

    Returns:
        None

    Description:
        This function sends a POST request to the API endpoint without the 'word' parameter.
        It validates the response status code to ensure it returns 400 (Bad Request).
    """
    # Set up the necessary data for the request
    url = f"http://{IP_ADDRESS}:5000/simplify_toggle"
    input_data = (
    "These misconceptions often stay from outdated information or "
    "myths that have been perpetuated over time."
    )
    # Set the query parameters without the 'word' parameter
    params = {
        "input": input_data
    }

    # Send a POST request to the API endpoint
    response = requests.post(url, data=params) 

    # Validate the response
    assert response.status_code == 400



def test_missing_input_parameter():
    """
    Test the case when the 'input' parameter is missing.

    Returns:
        None

    Description:
        This function sends a POST request to the API endpoint without the 'input' parameter.
        It validates the response status code to ensure it returns 400 (Bad Request).
    """
    # Set up the necessary data for the request
    url = f"http://{IP_ADDRESS}:5000/simplify_toggle"
    word = "myths"

    # Set the query parameters without the 'input' parameter
    params = {
        "word": word
    }

    # Send a POST request to the API endpoint
    response = requests.post(url, params=params)

    # Validate the response
    assert response.status_code == 400


def test_empty_parameters():
    """
    Test the case when both query parameters are empty.

    Returns:
        None

    Description:
        This function sends a POST request to the API endpoint with empty query parameters.
        It validates the response status code to ensure it returns 400 (Bad Request).
    """
    # Set up the necessary data for the request
    url = f"http://{IP_ADDRESS}:5000/simplify_toggle"

    # Set empty query parameters
    params = {}

    # Send a POST request to the API endpoint
    response = requests.post(url, params=params)

    # Validate the response
    assert response.status_code == 400

def test_simplified_sentence():
    """
    Test the simplification of a sentence using the 'simplify_toggle' API endpoint.

    Returns:
        None

    Description:
        This function sends a POST request to the API endpoint with predefined data.
        It validates the response status code, checks if the specified word is present in the response,
        compares the syllable count of the original sentence and simplified sentence,
        and prints the simplified sentence.
    """
    # Set up the necessary data for the request
    url = f"http://{IP_ADDRESS}:5000/simplify_toggle"
    word = "myths"
    input_data = (
    "These misconceptions often stay from outdated information or "
    "myths that have been perpetuated over time."
    )
    # Set the query parameters
    params = {
        "word": word,
        "input": input_data
    }

    # Send a POST request to the API endpoint
    response = requests.post(url, params=params)

    # Validate the response
    assert response.status_code == 200

    # Extract the response data
    data = response.text

    # Check if the word is present in the response
    assert word.lower() in data.lower()

    # Compare the syllable count of the original sentence and simplified sentence
    original_length = textstat.syllable_count(input_data)
    simplified_length = textstat.syllable_count(data)
    assert simplified_length < original_length

    # Print the simplified sentence
    print("Response:", data)


if __name__ == "__main__":
    pytest.main()
