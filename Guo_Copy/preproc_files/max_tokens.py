import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

# Download the NLTK tokenizer models (only needed the first time)
nltk.download('punkt')

def load_dataset_file(file_path):
    dataset = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            sequence = line.strip().split()  # Assuming each line is a sequence of tokens
            dataset.append(sequence)
    return dataset

def find_max_tokens(dataset):
    max_tokens = 0
    for sequence in dataset:
        num_tokens = len(sequence)
        if num_tokens > max_tokens:
            max_tokens = num_tokens
    return max_tokens

# Example file path (replace with your actual file path)
file_path = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/qari_train_trg.txt'

# Load dataset from file
dataset = load_dataset_file(file_path)

# Find max tokens in the dataset
max_tokens = find_max_tokens(dataset)

print(f"Max tokens in dataset: {max_tokens}")


# Function to count tokens in a dataset
def count_tokens_in_dataset(file_path):
    total_tokens = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Tokenize the current line
            tokens = word_tokenize(line)
            # Add the number of tokens in this line to the total count
            total_tokens += len(tokens)
    
    return total_tokens

# Path to the dataset file
dataset_file_path = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/trg_common_voice.txt'

# Count the tokens
total_token_count = count_tokens_in_dataset(dataset_file_path)
print(f"Total number of tokens in the dataset: {total_token_count}")

