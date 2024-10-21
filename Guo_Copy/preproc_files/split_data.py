import random
import os

def split_data(file_path, train_file, valid_file, split_ratio=(0.8, 0.2), shuffle=False):
    assert sum(split_ratio) == 1.0, "Split ratio should sum to 1.0"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        sentences = f.readlines()
    
    if shuffle:
        random.shuffle(sentences)
    
    total_count = len(sentences)
    train_count = int(total_count * split_ratio[0])
    valid_count = int(total_count * split_ratio[1])
    
    train_data = sentences[:train_count]
    valid_data = sentences[train_count:train_count + valid_count]
    
    write_data(train_file, train_data)
    write_data(valid_file, valid_data)

def write_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(data)

if __name__ == "__main__":
    input_file = '/Users/alanabusuttil/Projects/Guo_Copy/final_datasets/blended_dataset/target_blended_wordpiece.txt'
    train_file = 'final_datasets/blended_dataset/train_source_blended.trg'
    valid_file = 'final_datasets/blended_dataset/valid_source_blended.trg'
    
    split_data(input_file, train_file, valid_file)
    
    print(f"Data successfully split and saved into {train_file}, {valid_file}.")
