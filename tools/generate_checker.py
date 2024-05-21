import os

def check_folder(prompt_file, target_folder, min_images, output_file_missing, output_file_insufficient):
    with open(prompt_file, 'r') as f:
        lines = f.readlines()

    not_found_prompts = []
    insufficient_prompts = []

    for line in lines:
        if '--prompt' in line:
            prompt = line.split('"')[1]
            prompt_prefix = prompt.split(',')[0]
            matched_folder = None
            for folder in os.listdir(target_folder):
                if os.path.isdir(os.path.join(target_folder, folder)) and prompt_prefix in folder:
                    matched_folder = folder
                    break

            if matched_folder:
                matched_folder_path = os.path.join(target_folder, matched_folder)
                image_files = [f for f in os.listdir(matched_folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                if len(image_files) < min_images:
                    missing_count = min_images - len(image_files)
                    insufficient_prompts.append(f'--prompt "{prompt}" (lack {missing_count} images)')
            else:
                not_found_prompts.append(prompt)

    with open(output_file_missing, 'w') as f:
        for prompt in not_found_prompts:
            f.write(f'--prompt "{prompt}"\n')

    with open(output_file_insufficient, 'w') as f:
        for prompt in insufficient_prompts:
            f.write(f'{prompt}\n')

    print(f"Success. prompts that not found are recorded in {output_file_missing}，prompts that not completed are recorded in {output_file_insufficient}")

prompt_file = "/your/path/to/checker.txt"
target_folder = "/your/path/to/result"
min_images = 800
output_file_missing = "not_found_prompts.txt"
output_file_insufficient = "insufficient_prompts.txt"

check_folder(prompt_file, target_folder, min_images, output_file_missing, output_file_insufficient)