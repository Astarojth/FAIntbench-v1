import os
import json

def merge_json_files(folder_path, output_file):
    merged_data = {}

    # Traverse the directory and read each JSON file
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Assume keys in each JSON are unique and can be directly merged
                merged_data.update(data)

    # Write the merged data to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(merged_data, file, indent=4)

# Example usage
merge_json_files('light_1', 'merged_output1.json')
