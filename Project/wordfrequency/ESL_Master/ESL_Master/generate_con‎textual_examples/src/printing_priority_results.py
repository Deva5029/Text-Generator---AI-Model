def print_sorted_lists(sorted_similar, sorted_vocab):
    """ 
    Prints and returns a list of sentences with sentences with high vocabulary scores coming first, then sentences with comparable context, in that sequence. In the final list, all duplications are eliminated.

    Args: - sorted_similar: A list of sentences arranged in descending order according to the contextual similarity score.
      - sorted_vocab: A list of phrases arranged in descending order by vocabulary score.

    Returns: - final_list: A list of sentences arranged with high vocabulary score first and contextual similarity second. In the final list, all duplications are eliminated.
    """

    # Initialize an empty list to store the final sorted sentences
    final_list = []  

    # Iterate over the sentences in the sorted_similar list
    for sentence in sorted_similar:

        # Check if the sentence is present in sorted_vocab and not already in final_list
        if sentence in sorted_vocab and sentence not in final_list:

            # Add the sentence to final_list
            final_list.append(sentence)  

            # Remove the sentence from sorted_vocab to avoid duplicates
            sorted_vocab.remove(sentence)  
        
        # If the sentence is not already in final_list, add it to final_list
        elif sentence not in final_list:
            final_list.append(sentence)
    
    # Iterate over the remaining sentences in sorted_vocab
    for sentence in sorted_vocab:

        # If the sentence is not already in final_list, add it to final_list
        if sentence not in final_list:
            final_list.append(sentence)
    
    # Return the final sorted list of sentences
    return final_list  
