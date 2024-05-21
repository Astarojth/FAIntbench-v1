import json

# 读取json文件
with open('/data/hanjun/test/implicit/average_sdxl.json', 'r') as f:
    data = json.load(f)
f.close()
# 初始化新的json数据字典
new_data = {}

for key in data:
    if "left" in key:
        left_part, right_part = key.split(' with ')
        new_data[key] = {"left": {}, "right": {}}
        if "African" in left_part:
            left_score = data[key]["left"]["race"]["African"]
        if "East-Asian" in left_part:
            left_score = data[key]["left"]["race"]["East-asian"]
        if "European" in left_part:
            left_score = data[key]["left"]["race"]["European"]
        if "Latino" in left_part:
            left_score = data[key]["left"]["race"]["Latino"]
        if "South-Asian" in left_part:
            left_score = data[key]["left"]["race"]["South-Asian"]
        if "young" in left_part:
            left_score = data[key]["left"]["age"]["10~29 years old"]
        if "middle-aged" in left_part:
            left_score = data[key]["left"]["age"]["31~59 years old"]
        if "elderly" in left_part:
            left_score = data[key]["left"]["age"]["60 years old or older"]
        if "man"  in left_part or "male" in left_part:
            left_score = data[key]["left"]["gender"]["man"]
        if "woman"  in left_part or "female" in left_part:
            left_score = data[key]["left"]["gender"]["woman"]

        if "African" in right_part:
            right_score = data[key]["right"]["race"]["African"]
        if "East-Asian" in right_part:
            right_score = data[key]["right"]["race"]["East-asian"]
        if "European" in right_part:
            right_score = data[key]["right"]["race"]["European"]
        if "Latino" in right_part:
            right_score = data[key]["right"]["race"]["Latino"]
        if "South-Asian" in right_part:
            right_score = data[key]["right"]["race"]["South-Asian"]
        if "young" in right_part:
            right_score = data[key]["right"]["age"]["10~29 years old"]
        if " middle-aged" in right_part:
            right_score = data[key]["right"]["age"]["31~59 years old"]
        if "elderly" in right_part:
            right_score = data[key]["right"]["age"]["60 years old or older"]
        if "man" in right_part or "male" in right_part:
            right_score = data[key]["right"]["gender"]["man"]
        if "woman" in right_part or "female" in right_part:
            right_score = data[key]["right"]["gender"]["woman"]
        new_data[key] = right_score * 0.5 + left_score * 0.5

    else:
        if "African" in key:
            if "race" in data[key] and "African" in data[key]["race"]:
                new_data[key] = data[key]["race"]["African"]
        if "East-Asian" in key:
            if "race" in data[key] and "East-asian" in data[key]["race"]:
                new_data[key] = data[key]["race"]["East-asian"]
        if "European" in key:
            if "race" in data[key] and "European" in data[key]["race"]:
                new_data[key] = data[key]["race"]["European"]
        if "Latino" in key:
            if "race" in data[key] and "Latino" in data[key]["race"]:
                new_data[key] = data[key]["race"]["Latino"]
        if "South-Asian" in key:
            if "race" in data[key] and "South-Asian" in data[key]["race"]:
                new_data[key] = data[key]["race"]["South-Asian"]
        if "young" in key:
            if "age" in data[key] and "10~29 years old" in data[key]["age"]:
                new_data[key] = data[key]["age"]["10~29 years old"]
        if "middle-aged" in key:
            if "age" in data[key] and "31~59 years old" in data[key]["age"]:
                new_data[key] = data[key]["age"]["31~59 years old"]
        if "elderly" in key:
            if "age" in data[key] and "60 years old or older" in data[key]["age"]:
                new_data[key] = data[key]["age"]["60 years old or older"]
        if  "man" in key or "male" in key:
            if "gender" in data[key] and "man" in data[key]["gender"]:
                new_data[key] = data[key]["gender"]["man"]
        if "woman" or "female" in key:
            if "gender" in data[key] and "woman" in data[key]["gender"]:
                new_data[key] = data[key]["gender"]["woman"]
    



with open('/data/hanjun/test/explicit/ex_prompt_level.json', 'w') as f:
    json.dump(new_data, f, indent=4)
f.close()
print("generate successfully!")
