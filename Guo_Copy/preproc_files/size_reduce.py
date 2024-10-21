# Define the input and output file paths
input_file = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/human_synth/trg_synth_human.token.txt'  # Replace with the path to your input dataset
output_file = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/human_synth/trg_reduced_size.no.wordpiece.txt'  # Output file to store the first 8032 sentences

# Number of sentences to extract
num_sentences = 11248

# Open the input file for reading
with open(input_file, 'r', encoding='utf-8') as infile:
    # Read the first 8032 lines (sentences)
    sentences = [next(infile).strip() for _ in range(num_sentences)]

# Open the output file for writing
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Write each sentence on a new line
    for sentence in sentences:
        outfile.write(sentence + '\n')

print(f"The first {num_sentences} sentences have been written to {output_file}.")
