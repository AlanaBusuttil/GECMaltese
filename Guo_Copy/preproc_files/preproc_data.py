import os
import json
import string
import re
#from transformers import BertTokenizer
from tokeniser import MTWordTokenizer
tokenizer = MTWordTokenizer()

def remove_punctuation(text):
    punctuations = string.punctuation
    no_punct_text = ''.join([char for char in text if char not in punctuations])
    return no_punct_text

def tokenize_and_save_in_batches(input_file, output_file, batch_size=1000, tokenizer_name='bert-base-multilingual-cased'):
    # Initialize the BERT tokenizer
    # tokenizer = BertTokenizer.from_pretrained(tokenizer_name)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.readlines()

    total_lines = len(data)
    num_batches = (total_lines + batch_size - 1) // batch_size  # Ceiling division to get number of batches

    with open(output_file, 'w', encoding='utf-8') as f:
        for batch_num in range(num_batches):
            start_index = batch_num * batch_size
            end_index = min(start_index + batch_size, total_lines)
            batch_lines = data[start_index:end_index]

            tokenized_data = []
            for line in batch_lines:
                line_no_punct = remove_punctuation(line)
                tokenized_line = tokenizer.tokenize(line_no_punct)
                tokenized_data.append(" ".join(tokenized_line))

            # Write tokenized lines to the output file
            f.write("\n".join(tokenized_data) + "\n")
            print(f"Processed batch {batch_num + 1}/{num_batches}")

    print(f"Tokenized data saved to {output_file}")

# Example usage
input_file = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/compiled_output_trg_final.txt'  # Update with the path to your input file
output_file = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/compiled_output_trg_final_token.txt'  # Update with the path to your desired output file

tokenize_and_save_in_batches(input_file, output_file)

'''
# Function to read the dataset file and create a dictionary
def create_dictionary_from_file(file_path):
    # Step 1: Initialize the dictionary
    dictionary = Dictionary()
    
    # Step 2: Read the file and tokenize the text
    with open(file_path, 'r') as file:
        for line in file:
            # Tokenize the line into words
            tokens = re.findall(r'\b\w+\b', line.lower())
            # Add each token to the dictionary
            for token in tokens:
                dictionary.add_symbol(token)
                
    return dictionary

def create_dictionary_from_tokenized_file(file_path):
    # Step 1: Initialize the dictionary
    dictionary = Dictionary()
    
    # Step 2: Read the tokenized file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Assume tokens are space-separated in each line
            tokens = line.strip().split()
            # Add each token to the dictionary
            for token in tokens:
                dictionary.add_symbol(token)
                
    return dictionary

# Path to the dataset file
dataset_file_path = '/Users/alanabusuttil/Projects/Guo_Copy/src-trg/trg.token.txt'

# Create the dictionary from the dataset file
dictionary = create_dictionary_from_tokenized_file(dataset_file_path)

# Optional: Save the dictionary to a file
dictionary.save('/Users/alanabusuttil/Projects/Guo_Copy/src-trg/dict_token_trg.txt')

# Optional: Load the dictionary from a file
loaded_dictionary = Dictionary.load('/Users/alanabusuttil/Projects/Guo_Copy/src-trg/dict_token_trg.txt')

# Check the contents of the dictionary
print("Dictionary Contents:")
for i in range(len(dictionary)):
    print(f"Token: {dictionary[i]}, Count: {dictionary.count[i]}")
'''