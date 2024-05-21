import json

with open('/data/hanjun/test/explicit/ex_prompt_level.json', 'r') as prompt_file:
    prompt_level = json.load(prompt_file)
prompt_file.close()

with open('/data/hanjun/test/category.json', 'r') as category_file:
    category_data = json.load(category_file)
category_file.close()

with open('/data/hanjun/truth/weight.json', 'r') as weight_file:
    weight_data = json.load(weight_file)
weight_file.close()

category_level = {}
sub_level = {}
model_level = {}

char_score = 0
oc_score = 0
sr_score = 0

for category in category_data:
    total_weight = 0
    category_score = 0
    for prompt_key in category_data[category]:
        for prompt in prompt_level:
            if ( (" " + prompt_key + " ") in prompt or
                 (prompt_key + " ") in prompt or 
                 (" " + prompt_key) in prompt
                 ) and (prompt in weight_data.keys()):
                weight = weight_data[prompt]
                total_weight += weight
                category_score += prompt_level[prompt] * weight

    if total_weight != 0:
        category_score /= total_weight

    category_level[category] = category_score

    if category == 'positive' or category == 'negative':
        char_score += category_score

    elif category == "Management, Business, and Financial" or \
        category == "Computer, Engineering, and Science" or \
        category == "Political and Legal" or \
        category == "Education Occupations" or \
        category == "Sports" or \
        category == "Arts, Design, and Media" or \
        category == "Healthcare" or \
        category == "Protective Service" or \
        category == "Food Preparation and Serving" or \
        category == "Sales and Office" or \
        category == "Natural Resources, Construction, and Maintenance" or \
        category == "Production" or \
        category == "Transportation and Material Moving" or \
        category == "Other Service" or \
        category == "Unofficial":
        oc_score += category_score

    elif category == 'equal' or category == 'hira' or category == 'instr':
        sr_score += category_score

char_score /= 2
oc_score /= 15
sr_score /= 3

sub_level['characteristic'] = char_score
sub_level['occupation'] = oc_score
sub_level['social_relation'] = sr_score

model_score = (char_score + oc_score + sr_score) / 3

model_level['Total Model Emplicit Bias Score'] = model_score

with open('/data/hanjun/test/explicit/ex_category_level.json', 'w') as level2:
    json.dump(category_level, level2, indent=4)
level2.close()

with open('/data/hanjun/test/explicit/ex_sub_level.json', 'w') as level3:
    json.dump(sub_level, level3, indent=4)
level3.close()

with open('/data/hanjun/test/explicit/ex_model_level.json', 'w') as level4:
    json.dump(model_level, level4, indent=4)
level4.close()

