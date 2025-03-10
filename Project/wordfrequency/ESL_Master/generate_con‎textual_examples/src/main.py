from updated_chat_gpt_api import input_string_concatenation, calling_openai_api
from sort_examples_based_on_context import sort_sentences_by_similarity
from sorting_based_on_vocab import sort_based_on_vocab
from printing_priority_results import print_sorted_lists

def main():
    try:
        #Getting input word/phrase from the user
        user_input_prompt = input("Please enter the word/phrase you want information on: ")

        #Creating prompt for chatGPT with the word/phrase given by user
        gpt_prompt = input_string_concatenation(user_input_prompt)
        
        #To get the list of examples from chatGPT based on the prompt generated
        gpt_output = calling_openai_api(gpt_prompt) 

        #Sorting the list of examples on the basis of relevancy
        similar_sorted = sort_sentences_by_similarity(gpt_output, user_input_prompt)

        #Sorting the list of examples on the basis of user vocabulary
        vocabulary = ["apple", "ball", "cat", "dog", "elephant", "flower", "guitar", "hat", 
        "ice cream", "juice", "key", "lion", "moon", "nurse", "orange", "pizza", "queen", 
        "rainbow", "sun", "tiger", "umbrella", "violin", "whale", "xylophone", "yellow", "zebra"]

        vocab_sorted = sort_based_on_vocab(vocabulary, gpt_output)

        #Generating final list of examples from both the sorted lists by removing the examples that are overlapping
        final_examples = print_sorted_lists(similar_sorted, vocab_sorted)

        #Returning the final list of examples
        return final_examples
    
    except Exception as e:
        #Handling the exceptions that occur during the execution of code
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
