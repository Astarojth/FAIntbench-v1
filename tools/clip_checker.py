import os
import json
import shutil

# Set the paths to your JSON file, source directory, and destination directory
json_file_path = '/data/hanjun/process_sigma/Group_2/meta_checkpoint.json'
source_directory = '/data/hanjun/process_sigma/Group_2'
destination_directory = '/data/hanjun/result/sigma'

def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def move_matching_directories(json_data, src_dir, dest_dir):
    # Create destination directory if it does not exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Get all directories in the source directory
    all_directories = [d for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]
    
    # Loop through each top-level key in the JSON data
    for key in json_data.keys():
        # Check each directory to see if it contains the top-level key in its name
        for directory in all_directories:
            if key in directory:
                # Construct full paths for moving
                src_path = os.path.join(src_dir, directory)
                dest_path = os.path.join(dest_dir, directory)
                # Move directory
                shutil.move(src_path, dest_path)
                print(f'Moved directory {src_path} to {dest_path}')

# Load the JSON data
data = load_json_data(json_file_path)

# Move the directories
move_matching_directories(data, source_directory, destination_directory)
