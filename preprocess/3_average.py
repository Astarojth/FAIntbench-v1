import json

def process_json(input_filepath, output_filepath):
    with open(input_filepath, 'r') as file:
        data = json.load(file)

    def calculate_averages(image_data):
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

    average_results = {}

    for prompt, images in data.items():
        if prompt.lower().startswith('a'):
            image_data = [image_data for image_data in images.values()]
            average_results[prompt] = calculate_averages(image_data)
        elif prompt.lower().startswith('o'):
            image_data = [image_data for image_data in images.values()]
            average_results[prompt] = calculate_averages_with_sides(image_data)

    with open(output_filepath, 'w') as file:
        json.dump(average_results, file, indent=4)

    print(f"Processing complete, results saved to '{output_filepath}'")

process_json('meta_checkpoint.json', 'average_results.json')


