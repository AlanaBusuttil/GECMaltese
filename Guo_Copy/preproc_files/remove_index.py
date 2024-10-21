import re

# Function to remove the index, colon, and single space from each line
def remove_index(line):
    # Use regex to remove the index, colon, and single space
    cleaned_line = re.sub(r'^\d+:\s', '', line)
    return cleaned_line

# Function to process a file by reading, cleaning, and writing its content
def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        line_count = 0
        for line in infile:
            cleaned_line = remove_index(line)
            outfile.write(cleaned_line)
            line_count += 1
        return line_count

# File paths
src_input_path = '/netscratch/abusuttil/Guo_copy/src-trg/src_eith.txt'
trg_input_path = '/netscratch/abusuttil/Guo_copy/src-trg/trg_eith.txt'
src_output_path = 'src_eith_no_index.txt'
trg_output_path = 'trg_eith_no_index.txt'

# Process the src and trg files
src_line_count = process_file(src_input_path, src_output_path)
trg_line_count = process_file(trg_input_path, trg_output_path)

# Output the number of sentences processed
print(f"Processed {src_line_count} lines for source file.")
print(f"Processed {trg_line_count} lines for target file.")

# Ensure both files have the same number of lines
if src_line_count != trg_line_count:
    raise ValueError("The number of lines in the processed src_eith_no_index.txt and trg_eith_no_index.txt do not match")
else:
    print("Processing complete. Cleaned data has been saved to 'src_eith_no_index.txt' and 'trg_eith_no_index.txt'.")
