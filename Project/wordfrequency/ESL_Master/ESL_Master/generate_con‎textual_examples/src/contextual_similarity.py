import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

# Load pre-trained BERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
bert_model = AutoModel.from_pretrained("bert-base-uncased")

def get_sentence_embedding(sentence):
    """
    Use pre-trained BERT model to generate sentence embeddings (mathematical representation 
    of meaning of the sentence).

    Args:
        sentence (str): Sentence to generate its embedding.

    Returns:
        numpy.ndarray: numpy array representing the sentence embedding.

    Raises:
        ValueError: If the sentence is null or empty.
    """

    if sentence is None or not sentence.strip():
        raise ValueError("Sentence cannot be empty.")

    # Tokenize sentence and convert tokens to IDs
    input_ids = torch.tensor(tokenizer.encode(sentence)).unsqueeze(0)

    # Feed input IDs to BERT model and get last hidden state
    outputs = bert_model(input_ids)
    last_hidden_state = outputs.last_hidden_state

    # Compute mean of last hidden state across all tokens
    sentence_embeddings = torch.mean(last_hidden_state, dim=1)

    # Convert tensor to numpy array
    sentence_embeddings = sentence_embeddings.detach().numpy()

    return sentence_embeddings

def get_similarity_score(sentence1, sentence2):
    """
    Compare two sentence embeddings to find contextual similarity between them.

    Args:
        sentence1 (str): Sentence 1
        sentence2 (str): Sentence 2

    Returns:
        float: value between -1 to 1, where 1 indicates maximum similarity
    """
    # Compute cosine similarity between sentence embeddings
    embedding1 = get_sentence_embedding(sentence1)
    embedding2 = get_sentence_embedding(sentence2)
    similarity_score = np.dot(embedding1, embedding2.T) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))

    return similarity_score