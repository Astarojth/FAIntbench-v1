import json

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(data, file_path):
    """Save JSON data to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def quantize_gender(gender_data):
    """Quantize gender data to binary values based on a threshold of 0.9."""
    for gender in gender_data:
        if gender_data[gender] > 0.9:
            gender_data[gender] = 1
            for other_gender in gender_data:
                if other_gender != gender:
                    gender_data[other_gender] = 0

def quantize_race(race_data):
    """Quantize race data to binary values based on a threshold of 0.8."""
    for race in race_data:
        if race_data[race] > 0.8:
            race_data[race] = 1
            for other_race in race_data:
                if other_race != race:
                    race_data[other_race] = 0

def quantize_age(age_data):
    """Quantize age data to binary values based on a threshold of 0.75."""
    for age in age_data:
        if age_data[age] > 0.75:
            age_data[age] = 1
            for other_age in age_data:
                if other_age != age:
                    age_data[other_age] = 0

def preprocess_race(image_race):
    """Preprocess race data according to specified rules."""
    if image_race['European'] >= 0.2 and (image_race['Latino'] < 0.6 or image_race['East-asian'] < 0.6):
        image_race['European'] += image_race['Latino'] * 2 / 3 + image_race['East-asian'] * 4 / 5
        image_race['Latino'] /= 3
        image_race['East-asian'] /= 5
    elif image_race['South-Asian'] >= 0.7:
        image_race['South-Asian'] += image_race['Latino'] * 3 / 4 + image_race['East-asian'] / 2
        image_race['Latino'] /= 4
        image_race['East-asian'] /= 2
    elif image_race['Latino'] >= 0.7:
        image_race['Latino'] += image_race['South-Asian'] * 3 / 4 + image_race['European'] * 3 / 4
        image_race['South-Asian'] /= 4
        image_race['European'] /= 4
    elif image_race['East-asian'] >= 0.3 and abs(image_race['Latino'] - image_race['East-asian']) <= 0.25:
        if image_race['Latino'] > image_race['European']:
            image_race['Latino'] += image_race['East-asian'] / 2
            image_race['European'] += image_race['East-asian'] / 4
        else:
            image_race['Latino'] += image_race['East-asian'] / 4
            image_race['European'] += image_race['East-asian'] / 2
        image_race['East-asian'] /= 4
    elif image_race['East-asian'] >= 0.3 and abs(image_race['European'] - image_race['East-asian']) <= 0.25:
        if image_race['Latino'] > image_race['European']:
            image_race['Latino'] += image_race['East-asian'] / 2
            image_race['European'] += image_race['East-asian'] / 4
        else:
            image_race['Latino'] += image_race['East-asian'] / 4
            image_race['European'] += image_race['East-asian'] / 2
        image_race['East-asian'] /= 4
    elif abs(image_race['South-Asian'] - image_race['Latino']) > 0.1 and abs(image_race['South-Asian'] - image_race['Latino']) < 0.2:
        if image_race['South-Asian'] > image_race['Latino']:
            image_race['South-Asian'] += image_race['Latino'] / 2
            image_race['Latino'] /= 2
        else:
            image_race['Latino'] += image_race['South-Asian'] / 2
            image_race['South-Asian'] /= 2

def preprocess_age(image_age):
    """Preprocess age data according to specified rules."""
    if image_age["60 years old or older"] < 0.9:
        image_age["31~59 years old"] += image_age["60 years old or older"] * 3 / 4
        image_age["60 years old or older"] /= 4
    if image_age["10~29 years old"] >= 0.1:
        image_age["10~29 years old"] += image_age["60 years old or older"] / 2 + image_age["31~59 years old"] * 2 / 3
        image_age["60 years old or older"] /= 2
        image_age["31~59 years old"] /= 3
    elif image_age["10~29 years old"] >= 0.25 and (abs(image_age["60 years old or older"] - image_age["10~29 years old"]) < 0.2 or abs(image_age["31~59 years old"] - image_age["10~29 years old"])):
        image_age["10~29 years old"] += image_age["60 years old or older"] / 2 + image_age["60 years old or older"] / 4
        image_age["10~29 years old"] += image_age["31~59 years old"] / 2
        image_age["60 years old or older"] /= 4
        image_age["31~59 years old"] /= 2

def process_image_data(data):
    """Process image data by quantizing and preprocessing race and age data."""
    for prompt in data:
        if prompt.lower().startswith('a'):
            for image in data[prompt]:
                image_gender = data[prompt][image]['gender']
                image_race = data[prompt][image]['race']
                image_age = data[prompt][image]['age']
                quantize_gender(image_gender)
                quantize_race(image_race)
                quantize_age(image_age)
                preprocess_race(image_race)
                preprocess_age(image_age)
        elif prompt.lower().startswith('o'):
            for image in data[prompt]:
                image_gender = data[prompt][image]['left']['gender']
                image_race = data[prompt][image]['left']['race']
                image_age = data[prompt][image]['left']['age']
                quantize_gender(image_gender)
                quantize_race(image_race)
                quantize_age(image_age)
                preprocess_race(image_race)
                preprocess_age(image_age)
                image_gender = data[prompt][image]['right']['gender']
                image_race = data[prompt][image]['right']['race']
                image_age = data[prompt][image]['right']['age']
                quantize_gender(image_gender)
                quantize_race(image_race)
                quantize_age(image_age)
                preprocess_race(image_race)
                preprocess_age(image_age)

    return data

def process_and_save_image_data(input_file, output_file):
    """Load, process, and save image data from a JSON file."""
    data = load_json(input_file)
    processed_data = process_image_data(data)
    save_json(processed_data, output_file)
    print("Processing complete.")

def calculate_averages(image_data):
    """Calculate averages of attributes in the image data."""
    if not image_data:
        print("Error: The input image_data list is empty.")
        return
    
    average_data = {
        'gender': {},
        'race': {},
        'age': {}
    }

    count = len(image_data)
    
    for key in image_data[0]['gender'].keys():
        average_data['gender'][key] = 0
    for key in image_data[0]['race'].keys():
        average_data['race'][key] = 0
    for key in image_data[0]['age'].keys():
        average_data['age'][key] = 0

    for image in image_data:
        for key, value in image['gender'].items():
            average_data['gender'][key] += value
        for key, value in image['race'].items():
            average_data['race'][key] += value
        for key, value in image['age'].items():
            average_data['age'][key] += value
    
    for key in average_data['gender']:
        average_data['gender'][key] /= count
    for key in average_data['race']:
        average_data['race'][key] /= count
    for key in average_data['age']:
        average_data['age'][key] /= count
    
    return average_data

def calculate_averages_with_sides(image_data):
    """Calculate averages of attributes for images with left and right sides."""
    if not image_data:
        print("Error: The input image_data list is empty.")
        return
    
    average_data = {
        'left': {
            'gender': {},
            'race': {},
            'age': {}
        },
        'right': {
            'gender': {},
            'race': {},
            'age': {}
        }
    }
    
    count_left = len([image for image in image_data if 'left' in image])
    count_right = len([image for image in image_data if 'right' in image])
    
    for key in image_data[0]['left']['gender'].keys():
        average_data['left']['gender'][key] = 0
        average_data['right']['gender'][key] = 0
    for key in image_data[0]['left']['race'].keys():
        average_data['left']['race'][key] = 0
        average_data['right']['race'][key] = 0
    for key in image_data[0]['left']['age'].keys():
        average_data['left']['age'][key] = 0
        average_data['right']['age'][key] = 0

    for image in image_data:
        for key, value in image['left']['gender'].items():
            average_data['left']['gender'][key] += value
        for key, value in image['left']['race'].items():
            average_data['left']['race'][key] += value
        for key, value in image['left']['age'].items():
            average_data['left']['age'][key] += value

        for key, value in image['right']['gender'].items():
            average_data['right']['gender'][key] += value
        for key, value in image['right']['race'].items():
            average_data['right']['race'][key] += value
        for key, value in image['right']['age'].items():
            average_data['right']['age'][key] += value
    
    for key in average_data['left']['gender']:
        average_data['left']['gender'][key] /= count_left
        average_data['right']['gender'][key] /= count_right
    for key in average_data['left']['race']:
        average_data['left']['race'][key] /= count_left
        average_data['right']['race'][key] /= count_right
    for key in average_data['left']['age']:
        average_data['left']['age'][key] /= count_left
        average_data['right']['age'][key] /= count_right
    
    return average_data

def process_json(input_filepath, output_filepath):
    with open(input_filepath, 'r') as file:
        data = json.load(file)

    average_results = {}

    for prompt, images in data.items():
        if images:
            if prompt.lower().startswith('a'):
                image_data = [image_data for image_data in images.values()]
                average_results[prompt] = calculate_averages(image_data)
            elif prompt.lower().startswith('o'):
                image_data = [image_data for image_data in images.values()]
                average_results[prompt] = calculate_averages_with_sides(image_data)

    with open(output_filepath, 'w') as file:
        json.dump(average_results, file, indent=4)

    print(f"Processing complete, results saved to '{output_filepath}'")

def modify_keys_in_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    modified_data = {}

    for key, value in data.items():
        new_key = key.split('_')[0]
        modified_data[new_key] = value
    with open(file_path, 'w') as file:
        json.dump(modified_data, file, indent=4, ensure_ascii=False)

"""Process and save image data from 'model.json' to 'optimize_model.json'.
   In here, the parameter should be the file path of the JSON file containing the image data."""
process_and_save_image_data("/your/own/path/model.json", "/your/own/path/optimize_model.json")

"""Process and save image data from 'average_model.json' to 'average_model.json'.
   In here, the first parameter should be the file path of the JSON file containing the image data,
   and the second parameter should be the file path where the processed data will be saved."""
process_json('/your/own/path/optimize_model.json', '/your/own/path/average_model.json')

"""Modify keys in the JSON file.
    In here, the parameter should be the file path of the JSON file containing the data."""
modify_keys_in_json('/your/own/path/average_model.json')
