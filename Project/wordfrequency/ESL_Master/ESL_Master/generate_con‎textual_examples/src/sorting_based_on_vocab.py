
import re


def sort_based_on_vocab(vocabulary, example):
  """
This function uses the Chat GPT examples and sorts them according to the user's vocabulary.
Args: 
      vocabulary(list): It is list that contains all the words that user is familier with. list named vocab is an test variable for vocabulary.
      example(list): List that contains examples provided by Chat GPT. List named ex is a test variable for examples.
Returns:
      examples(list): It is list of examples that is sorted based on user's vocabulary.
  """
  if example is None or not example.strip():
      raise ValueError("Sentence cannot be empty.")
  # c are used to count the amount of words in an example that are also in the user's vocabulary.
  c, i, j = 0, 0, 0
  # it is a list that containe how many words are their in a sentence from user vocabulary
  list_of_word_counts = []
  # vocab is list of user's vocabulary
  vocab = vocabulary
  #ex is list of example provided by Chat GPT 
  ex = example

  for j in range(len(ex)):
    for i in range(len(vocab)):
        if(re.findall(vocab[i], ex[j], flags = re.IGNORECASE)):
          c = c + 1  
    list_of_word_counts.append(c)
    c = 0    
  res = {ex[i]: list_of_word_counts[i] for i in range(len(ex))}
  new = dict(sorted(res.items(), key = lambda x: x[1], reverse = True))
  examples = list(new.keys())   
  return examples