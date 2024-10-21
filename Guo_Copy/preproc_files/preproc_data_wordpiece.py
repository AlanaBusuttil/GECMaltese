import os
import string
import re
#from fairseq.data import Dictionary
from transformers import BertTokenizer

def remove_punctuation(text):
    # Define the set of punctuation characters
    punctuations = string.punctuation
    
    # Remove punctuation characters from the text
    no_punct_text = ''.join([char for char in text if char not in punctuations])
    
    return no_punct_text

def tokenize_and_save(input_file, output_file, tokenizer_name='bert-base-multilingual-cased'):
    # Initialize the BERT tokenizer for wordpiece tokenization
    tokenizer = BertTokenizer.from_pretrained(tokenizer_name)
    
    # Read the input dataset
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.readlines()

    tokenized_data = []

    # Tokenize each line in the dataset after removing punctuation
    for line in data:
        # Remove punctuation from the line
        line_no_punct = remove_punctuation(line)
        
        # Tokenize the cleaned line using BERT tokenizer (wordpiece tokenization)
        tokenized_line = tokenizer.tokenize(line_no_punct.strip())
        tokenized_data.append(tokenized_line)

    # Save the tokenized dataset to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        for tokenized_line in tokenized_data:
            f.write(" ".join(tokenized_line) + "\n")

    print(f"Tokenized data saved to {output_file}")

'''
def create_dictionary_from_tokenized_file(file_path):
    # Step 1: Initialize the dictionary
    dictionary = Dictionary()

    # Step 2: Read the tokenized file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Tokenize the line into wordpieces using space separation
            tokens = line.strip().split()
            # Add each token to the dictionary
            for token in tokens:
                dictionary.add_symbol(token)

    return dictionary
'''
# Example usage
input_file = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/blended_dataset/target_blended.txt'  # Update with the path to your input file
output_file = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/blended_dataset/target_blended_wordpiece.txt'  # Update with the path to your desired output file

# Tokenize and save the input file using BERT tokenizer
tokenize_and_save(input_file, output_file)

'''
# Path to the tokenized dataset file
dataset_file_path = '/Users/alanabusuttil/Projects/Guo_Copy/src-trg/src.token.txt'


# Create the dictionary from the tokenized dataset file
dictionary = create_dictionary_from_tokenized_file(dataset_file_path)

# Optional: Save the dictionary to a file
dictionary.save('/Users/alanabusuttil/Projects/Guo_Copy/src-trg/dict_token_src.txt')

# Optional: Load the dictionary from a file
loaded_dictionary = Dictionary.load('/Users/alanabusuttil/Projects/Guo_Copy/src-trg/dict_token_src.txt')

# Check the contents of the dictionary
print("Dictionary Contents:")
for i in range(len(dictionary)):
    print(f"Token: {dictionary[i]}, Count: {dictionary.count[i]}")
'''