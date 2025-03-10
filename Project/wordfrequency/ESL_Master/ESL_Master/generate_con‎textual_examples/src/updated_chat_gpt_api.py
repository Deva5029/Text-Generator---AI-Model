import openai
import logging
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("API_KEY")


def input_string_concatenation(users_input):
    """
    Concatenates 2 strings, 1 being the users input for which the user wants the
    contextual information on, and the other being the deafult input for the chat
    gpt to process.

    Args:
        users_input(str): a word or a phrase

    Returns:
        CHAT_GPT_INPUT(str): which is a concatenated string
    """
    return "Give me 20 contextual examples of using " + users_input + " in a sentence. Answer in paragraph form"


def calling_openai_api(input_prompt):
    """
    Args:
        input_prompt(str): input for chat gpt to process.

    Returns:
        output_list(list): The response from chat gpt api in a list.
    """
    try:
        output_list = []
        MODEL_ENGINE = "text-davinci-003"
        completion = openai.Completion.create(
            engine=MODEL_ENGINE,
            prompt=input_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text

        output_list.append(response.split("\n"))
        output_list = list(filter(None, output_list))
        output_list = output_list[0][2:]

        final_list = []
        for i in range(0, len(output_list)):
            j = i + 1
            final_list.append(output_list[i].replace(str(j) + ". ", ""))

        return final_list
    except openai.error.OpenAIError as e:
        logging.error("An error occurred while calling the OpenAI API: %s", e)
        return None
