import json

def process_and_update_json(input_filepath, output_filepath):
    with open(input_filepath, 'r') as f:
        data = json.load(f)
    new_data = {}
    keys_to_delete = []
    for key in data:
        if key.startswith('O') and 'with' in key:
            left_part, right_part = key.split(' with ')
            left_part = left_part.strip()
            right_part = right_part.strip()
            left_content = data[key].get('left', {})
            right_content = data[key].get('right', {})
            new_data[left_part] = left_content
            new_data[right_part] = right_content
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del data[key]
    data.update(new_data)

    explicit=["man", "woman", "young", "male", "female", "elderly", "middle-aged", "African", "East-Asian", "South-Asian", "European", "Latino"]
    keys_to_delete = [key for key in data if any(substring in key for substring in explicit)]
    for key in keys_to_delete:
        del data[key]
    with open(output_filepath, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Processing complete, results saved to '{output_filepath}'")

process_and_update_json('average_cascade.json', 'cascade_data_eta.json')
