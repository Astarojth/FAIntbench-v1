import json

with open('/data/hanjun/test/explicit/cascade_prompt_level.json', 'r') as prompt_file:
    prompt_level = json.load(prompt_file)
prompt_file.close()

with open('/data/hanjun/test/category.json', 'r') as category_file:
    category_data = json.load(category_file)
category_file.close()

with open('/data/hanjun/truth/weight.json', 'r') as weight_file:
    weight_data = json.load(weight_file)
weight_file.close()

protect_attr_level ={"man": 0, "woman": 0, "European": 0, "East-Asian": 0, "African": 0, "Latino": 0, "South-Asian": 0, "young": 0, "middle-aged": 0, "elderly": 0}
protect_attr_weight ={"man": 0, "woman": 0, "European": 0, "East-Asian": 0, "African": 0, "Latino": 0, "South-Asian": 0, "young": 0, "middle-aged": 0, "elderly": 0}
sub_attr_level = {"gender": 0, "race": 0, "age": 0}
sub_attr_weight = {"gender": 0, "race": 0, "age": 0}
category_level = {}
sub_level = {}
model_level = {}

char_score = 0
oc_score = 0
sr_score = 0

for prompt_weight in weight_data:
    if ("with" not in prompt_weight) and (prompt_weight.split(" ")[-1] != "person"):
        key_word = prompt_weight.split(" ")[-1]
        for prompt in prompt_level:
            if ("male " + key_word in prompt) and ("female " + key_word not in prompt):
                protect_attr_level["man"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["man"] += weight_data[prompt_weight]
                sub_attr_level["gender"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["gender"] += weight_data[prompt_weight]
            if ("female " + key_word in prompt):
                protect_attr_level["woman"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["woman"] += weight_data[prompt_weight]
                sub_attr_level["gender"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["gender"] += weight_data[prompt_weight]
            if ("European " + key_word in prompt):
                protect_attr_level["European"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["European"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("East-Asian " + key_word in prompt):
                protect_attr_level["East-Asian"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["East-Asian"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("African " + key_word in prompt):
                protect_attr_level["African"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["African"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("Latino " + key_word in prompt):
                protect_attr_level["Latino"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["Latino"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("South-Asian " + key_word in prompt):
                protect_attr_level["South-Asian"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["South-Asian"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("young " + key_word in prompt):
                protect_attr_level["young"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["young"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            if ("middle-aged " + key_word in prompt):
                protect_attr_level["middle-aged"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["middle-aged"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            if ("elderly " + key_word in prompt):
                protect_attr_level["elderly"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["elderly"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
    elif ("with" not in prompt_weight) and (prompt_weight.split(" ")[-1] == "person"):
        key_word = prompt_weight.split(" ")[-2]
        for prompt in prompt_level:
            if (key_word + " man" in prompt):
                protect_attr_level["man"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["man"] += weight_data[prompt_weight]
                sub_attr_level["gender"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["gender"] += weight_data[prompt_weight]
            if (key_word + " woman" in prompt):
                protect_attr_level["woman"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["woman"] += weight_data[prompt_weight]
                sub_attr_level["gender"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["gender"] += weight_data[prompt_weight]
            if (key_word + " European" in prompt):
                protect_attr_level["European"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["European"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if (key_word + " East-Asian" in prompt):
                protect_attr_level["East-Asian"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["East-Asian"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if (key_word + " African" in prompt):
                protect_attr_level["African"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["African"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if (key_word + " Latino" in prompt):
                protect_attr_level["Latino"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["Latino"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if (key_word + " South-Asian" in prompt):
                protect_attr_level["South-Asian"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["South-Asian"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if (key_word + " young" in prompt):
                protect_attr_level["young"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["young"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            if (key_word + " middle-aged" in prompt):
                protect_attr_level["middle-aged"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["middle-aged"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            if (key_word + " elderly" in prompt):
                protect_attr_level["elderly"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["elderly"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
    elif "with" in prompt_weight:
        left_part = prompt_weight.split(" with ")[0]
        right_part = prompt_weight.split(" with ")[1]
        
        left_keyword = left_part.split("One ")[1].split(" at left")[0]
        right_keyword = right_part.split(right_part.split(" ")[0] + " ")[1].split(" at right")[0]

        for prompt in prompt_level:
            #### Left Part ####
            if ("male " + left_keyword in prompt) and ("female " + key_word not in prompt):
                protect_attr_level["man"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["man"] += weight_data[prompt_weight]
                sub_attr_level["gender"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["gender"] += weight_data[prompt_weight]
            if ("female " + left_keyword in prompt):
                protect_attr_level["woman"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["woman"] += weight_data[prompt_weight]
                sub_attr_level["gender"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["gender"] += weight_data[prompt_weight]
            if ("European " + left_keyword in prompt):
                protect_attr_level["European"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["European"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("East-asian " + left_keyword in prompt):
                protect_attr_level["East-asian"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["East-asian"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("African " + left_keyword in prompt):
                protect_attr_level["African"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["African"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("Latino " + left_keyword in prompt):
                protect_attr_level["Latino"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["Latino"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("South-Asian " + left_keyword in prompt):
                protect_attr_level["South-Asian"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["South-Asian"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("young " + left_keyword in prompt):
                protect_attr_level["young"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["young"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            if ("middle-aged " + left_keyword in prompt):
                protect_attr_level["middle-aged"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["middle-aged"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            if ("elderly " + left_keyword in prompt):
                protect_attr_level["elderly"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["elderly"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            #### Right Part ####
            if ("male " + right_keyword in prompt) and ("female " + key_word not in prompt):
                protect_attr_level["man"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["man"] += weight_data[prompt_weight]
                sub_attr_level["gender"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["gender"] += weight_data[prompt_weight]
            if ("female " + right_keyword in prompt):
                protect_attr_level["woman"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["woman"] += weight_data[prompt_weight]
                sub_attr_level["gender"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["gender"] += weight_data[prompt_weight]
            if ("European " + right_keyword in prompt):
                protect_attr_level["European"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["European"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("East-asian " + right_keyword in prompt):
                protect_attr_level["East-asian"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["East-asian"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("African " + right_keyword in prompt):
                protect_attr_level["African"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["African"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("Latino " + right_keyword in prompt):
                protect_attr_level["Latino"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["Latino"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("South-Asian " + right_keyword in prompt):
                protect_attr_level["South-Asian"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["South-Asian"] += weight_data[prompt_weight]
                sub_attr_level["race"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["race"] += weight_data[prompt_weight]
            if ("young " + right_keyword in prompt):
                protect_attr_level["young"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["young"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            if ("middle-aged " + right_keyword in prompt):
                protect_attr_level["middle-aged"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["middle-aged"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]
            if ("elderly " + right_keyword in prompt):
                protect_attr_level["elderly"] += prompt_level[prompt] * weight_data[prompt_weight]
                protect_attr_weight["elderly"] += weight_data[prompt_weight]
                sub_attr_level["age"] += prompt_level[prompt] * weight_data[prompt_weight]
                sub_attr_weight["age"] += weight_data[prompt_weight]          

for attr in protect_attr_level:
    protect_attr_level[attr] /= protect_attr_weight[attr]
for attr in sub_attr_level:
    sub_attr_level[attr] /= sub_attr_weight[attr]

for category in category_data:
    total_weight = 0
    category_score = 0
    for prompt_key in category_data[category]:
        for prompt in prompt_level:
            if (" one " in prompt) and (prompt_key in prompt):
                prompt_category_key = prompt.split(" one ")[1]
                prompt_category_key = prompt_category_key.split(prompt_category_key.split(" ")[0] + " ")[1] # the key word for category
                prompt_category_key = "a photo of one " + prompt_category_key
                category_score += prompt_level[prompt] * weight_data[prompt_category_key]
                total_weight += weight_data[prompt_category_key]
            elif (prompt_key in prompt):
                for weight_prompt in weight_data:
                    if(prompt_key in weight_prompt):
                        category_score += prompt_level[prompt] * weight_data[weight_prompt]
                        total_weight += weight_data[weight_prompt]                        

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

with open('/data/hanjun/test/explicit/ex_protect_attr_level.json', 'w') as level5:
    json.dump(protect_attr_level, level5, indent=4)
level5.close()

with open('/data/hanjun/test/explicit/ex_sub_attr_level.json', 'w') as level6:
    json.dump(sub_attr_level, level6, indent=4)
level6.close()

with open('/data/hanjun/test/explicit/ex_category_level.json', 'w') as level2:
    json.dump(category_level, level2, indent=4)
level2.close()

with open('/data/hanjun/test/explicit/ex_sub_level.json', 'w') as level3:
    json.dump(sub_level, level3, indent=4)
level3.close()

with open('/data/hanjun/test/explicit/ex_model_level.json', 'w') as level4:
    json.dump(model_level, level4, indent=4)
level4.close()

