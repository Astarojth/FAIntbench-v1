import json

def load_json(filepath):
    """Load JSON data from a file."""
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json(data, filepath):
    """Save JSON data to a file."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def process_data(data):
    """Process the input data to calculate scores based on specific keywords."""
    new_data = {}
    for key in data:
        if "left" in key:
            left_part, right_part = key.split(' with ')
            left_score = right_score = 0
            
            # Determine left score
            if "African" in left_part:
                left_score = data[key]["left"]["race"]["African"]
                new_data[left_part] = left_score
            elif "East-Asian" in left_part:
                left_score = data[key]["left"]["race"]["East-asian"]
                new_data[left_part] = left_score
            elif "European" in left_part:
                left_score = data[key]["left"]["race"]["European"]
                new_data[left_part] = left_score
            elif "Latino" in left_part:
                left_score = data[key]["left"]["race"]["Latino"]
                new_data[left_part] = left_score
            elif "South-Asian" in left_part:
                left_score = data[key]["left"]["race"]["South-Asian"]
                new_data[left_part] = left_score
            elif "young" in left_part:
                left_score = data[key]["left"]["age"]["10~29 years old"]
                new_data[left_part] = left_score
            elif "middle-aged" in left_part:
                left_score = data[key]["left"]["age"]["31~59 years old"]
                new_data[left_part] = left_score
            elif "elderly" in left_part:
                left_score = data[key]["left"]["age"]["60 years old or older"]
                new_data[left_part] = left_score
            elif " man" in left_part or " male" in left_part:
                left_score = data[key]["left"]["gender"]["man"]
                new_data[left_part] = left_score
            elif " woman" in left_part or " female" in left_part:
                left_score = data[key]["left"]["gender"]["woman"]
                new_data[left_part] = left_score

            # Determine right score
            if "African" in right_part:
                right_score = data[key]["right"]["race"]["African"]
                new_data[right_part] = right_score
            elif "East-Asian" in right_part:
                right_score = data[key]["right"]["race"]["East-asian"]
                new_data[right_part] = right_score
            elif "European" in right_part:
                right_score = data[key]["right"]["race"]["European"]
                new_data[right_part] = right_score
            elif "Latino" in right_part:
                right_score = data[key]["right"]["race"]["Latino"]
                new_data[right_part] = right_score
            elif "South-Asian" in right_part:
                right_score = data[key]["right"]["race"]["South-Asian"]
                new_data[right_part] = right_score
            elif "young" in right_part:
                right_score = data[key]["right"]["age"]["10~29 years old"]
                new_data[right_part] = right_score
            elif "middle-aged" in right_part:
                right_score = data[key]["right"]["age"]["31~59 years old"]
                new_data[right_part] = right_score
            elif "elderly" in right_part:
                right_score = data[key]["right"]["age"]["60 years old or older"]
                new_data[right_part] = right_score
            elif " man" in right_part or " male" in right_part:
                right_score = data[key]["right"]["gender"]["man"]
                new_data[right_part] = right_score
            elif " woman" in right_part or " female" in right_part:
                right_score = data[key]["right"]["gender"]["woman"]
                new_data[right_part] = right_score

            
            

        else:
            if "African" in key:
                if "race" in data[key] and "African" in data[key]["race"]:
                    new_data[key] = data[key]["race"]["African"]
            elif "East-Asian" in key:
                if "race" in data[key] and "East-asian" in data[key]["race"]:
                    new_data[key] = data[key]["race"]["East-asian"]
            elif "European" in key:
                if "race" in data[key] and "European" in data[key]["race"]:
                    new_data[key] = data[key]["race"]["European"]
            elif "Latino" in key:
                if "race" in data[key] and "Latino" in data[key]["race"]:
                    new_data[key] = data[key]["race"]["Latino"]
            elif "South-Asian" in key:
                if "race" in data[key] and "South-Asian" in data[key]["race"]:
                    new_data[key] = data[key]["race"]["South-Asian"]
            elif "young" in key:
                if "age" in data[key] and "10~29 years old" in data[key]["age"]:
                    new_data[key] = data[key]["age"]["10~29 years old"]
            elif "middle-aged" in key:
                if "age" in data[key] and "31~59 years old" in data[key]["age"]:
                    new_data[key] = data[key]["age"]["31~59 years old"]
            elif "elderly" in key:
                if "age" in data[key] and "60 years old or older" in data[key]["age"]:
                    new_data[key] = data[key]["age"]["60 years old or older"]
            elif " man" in key or " male" in key:
                if "gender" in data[key] and "man" in data[key]["gender"]:
                    new_data[key] = data[key]["gender"]["man"]
            elif " woman" in key or " female" in key:
                if "gender" in data[key] and "woman" in data[key]["gender"]:
                    new_data[key] = data[key]["gender"]["woman"]
    return new_data

def generate_new_data(input_filepath, output_filepath):
    """Load data, process it, and save the new data to a file."""
    data = load_json(input_filepath)
    new_data = process_data(data)
    save_json(new_data, output_filepath)
    print("Generation successful!")

# Example function call
generate_new_data('average_cascade.json', 'cascade_prompt_level.json')