# API Test Cases

This repository contains test cases for testing an API endpoint that simplifies sentences using simpler vocabulary. The test cases are implemented using the pytest framework and make use of the requests library to send HTTP requests to the API.

## Getting Started

These instructions will guide you on running the test cases locally.

### Prerequisites

- Python 3.x
- pytest package
- requests package
- textstat package
- dotenv package

### Installation


2. Install the required packages:

pip install pytest requests textstat dotenv


3. Create a `.env` file in the root directory of the project and add the following environment variables:

IP_ADDRESS=<your-ip-address>


Replace `<your-ip-address>` with the IP address where the API is hosted.

## Running the Tests

1. Open a terminal and navigate to the project's root directory.
2. Run the following command to execute the test cases:
pytest test_cases_userstory6.py


The tests will be executed, and the results will be displayed in the terminal.

## Test Cases

### 1. `test_my_api_endpoint()`

- Description: Tests the API endpoint by sending a POST request with valid parameters and validates the response.
- Expected Result: The response status code should be 200 (OK). The response data should contain the word specified in the request.

### 2. `test_missing_word_parameter()`

- Description: Tests the API endpoint by sending a POST request with a missing 'word' parameter and validates the response.
- Expected Result: The response status code should be 400 (Bad Request).

### 3. `test_missing_input_parameter()`

- Description: Tests the API endpoint by sending a POST request with a missing 'input' parameter and validates the response.
- Expected Result: The response status code should be 400 (Bad Request).

### 4. `test_empty_parameters()`

- Description: Tests the API endpoint by sending a POST request with empty parameters and validates the response.
- Expected Result: The response status code should be 400 (Bad Request).

### 5. `test_simplified_sentence()`

- Description: Tests the API endpoint by sending a POST request with valid parameters and validates the response. Also compares the syllable count of the original sentence and the simplified sentence.
- Expected Result: The response status code should be 200 (OK). The response data should contain the word specified in the request. The syllable count of the simplified sentence should be less than the syllable count of the original sentence.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
