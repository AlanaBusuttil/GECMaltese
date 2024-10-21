# Define file paths
SOURCE_FILE = "predictions_final_model.txt"
TARGET_FILE = "targets_final_model.txt"

# Initialize the counter for exact matches
exact_match_count = 0

# Read both files line-by-line and compare them
with open(SOURCE_FILE, "r", encoding="utf-8") as source_file, open(TARGET_FILE, "r", encoding="utf-8") as target_file:
    # Read lines from both files
    source_lines = source_file.readlines()
    target_lines = target_file.readlines()

# Ensure both files have the same number of lines
if len(source_lines) != len(target_lines):
    print(f"Warning: The source file has {len(source_lines)} lines, while the target file has {len(target_lines)} lines.")

# Loop through lines to count exact matches
for src_line, tgt_line in zip(source_lines, target_lines):
    if src_line.strip() == tgt_line.strip():
        exact_match_count += 1

# Print the total number of exact matches
print(f"Total exact matches: {exact_match_count} out of {len(source_lines)}")
