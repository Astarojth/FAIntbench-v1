import os
import shutil

def process_prompts(prompt_file_path, image_directory, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(prompt_file_path, 'r') as file:
        prompts = file.readlines()

    for prompt in prompts:
        prompt_content = prompt.strip()
        if '--prompt' in prompt_content:
            # Extract the entire content inside the quotes
            start_quote = prompt_content.find('"') + 1
            end_quote = prompt_content.find('"', start_quote)
            full_prompt = prompt_content[start_quote:end_quote]

            # Extract the part of the prompt before the first comma
            first_comma = full_prompt.find(',')
            prompt_key = full_prompt[:first_comma] if first_comma != -1 else full_prompt

            # Create directory for this prompt
            folder_name = '_'.join(full_prompt.split(', ')[:3])  # Take first three items split by comma and space
            folder_path = os.path.join(output_directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Copy relevant files to the corresponding folder
            for filename in os.listdir(image_directory):
                if prompt_key in filename:
                    src_path = os.path.join(image_directory, filename)
                    dest_path = os.path.join(folder_path, filename)
                    shutil.move(src_path, dest_path)

# Example usage
prompt_file_path = '/your/own/path/checker.txt'
image_directory = '/your/own/path/sigma/output'
output_directory = '/your/own/path/temp'
process_prompts(prompt_file_path, image_directory, output_directory)