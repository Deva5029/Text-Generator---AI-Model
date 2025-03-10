from contextual_similarity import get_similarity_score

def sort_sentences_by_similarity(sentences, input_sentence):
    """
    Args:
            sentences(str): List of the string
            input_sentence(str): string input 

    Returns:
            str: Sorted List of string
    """
    if not sentences:
        raise ValueError("The list of sentences is empty.")
    if not input_sentence:
        raise ValueError("The input sentence is empty.")
    
    # Compute similarity scores for all sentences
    similarity_scores = []
    for sentence in sentences:
        score = get_similarity_score(input_sentence, sentence)
        similarity_scores.append((sentence, score))

    # Sort sentences by similarity score in descending order
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    sorted_sentences = []
    for score in sorted_scores:
        sorted_sentences.append(score[0])

    return sorted_sentences
