import json

with open("/data/hanjun/test/explicit/average_sdxl.json") as f1:
    data = json.load(f1)
f1.close()

for prompt in data:
    for image in data[prompt]:
        image_race = data[prompt][image]['race']
        image_age = data[prompt][image]['age']
        # quantainize
        for race in image_race:
            if image_race[race] > 0.8:
                image_race[race] = 1
                for other_race in image_race:
                    if other_race != race:
                        image_race[other_race] = 0
                        
        for age in image_age:
            if image_age[age] > 0.75:
                image_age[age] = 1
                for other_age in image_age:
                    if other_age != age:
                        image_age[other_age] = 0

        # preprocess race
        if image_race['European']>=0.2 and image_race['Latino'] < 0.6:
            image_race['European'] = image_race['European'] + image_race['Latino']/2
            image_race['Latino'] /= 2
        
        elif image_race['East-asian'] >= 0.3 and abs(image_race['Latino'] - image_race['East-asian']) <= 0.25:
            if(image_race['Latino'] > image_race['European']):
                image_race['Latino'] = image_race['Latino'] + image_race['East-asian'] * (1/2)
                image_race['European'] = image_race['European'] + image_race['East-asian'] * (1/4)
            else:
                image_race['Latino'] = image_race['Latino'] + image_race['East-asian'] * (1/4)
                image_race['European'] = image_race['European'] + image_race['East-asian'] * (1/2)

            image_race['East-asian'] = image_race['East-asian'] / 4

        elif image_race['East-asian'] >= 0.3 and abs(image_race['European'] - image_race['East-asian']) <= 0.25:
            if(image_race['Latino'] > image_race['European']):
                image_race['Latino'] = image_race['Latino'] + image_race['East-asian'] * (1/2)
                image_race['European'] = image_race['European'] + image_race['East-asian'] * (1/4)
            else:
                image_race['Latino'] = image_race['Latino'] + image_race['East-asian'] * (1/4)
                image_race['European'] = image_race['European'] + image_race['East-asian'] * (1/2)

            image_race['East-asian'] = image_race['East-asian'] / 4
        
        elif abs(image_race['South-Asian'] - image_race['Latino']) > 0.1 and abs(image_race['South-Asian'] - image_race['Latino']) < 0.2:
            if image_race['South-Asian'] > image_race['Latino']:
                image_race['South-Asian'] = image_race['South-Asian'] + image_race['Latino']/2
                image_race['Latino'] /= 2
            else:
                image_race['Latino'] = image_race['Latino'] + image_race['South-Asian']/2
                image_race['South-Asian'] /= 2

        # preprocess age
        if image_age["60 years old or older"] - image_age["31~59 years old"] < 0.3:
            image_age["31~59 years old"] = image_age["31~59 years old"] + image_age["60 years old or older"]/2
            image_age["60 years old or older"] /= 2
        
        elif image_age["10~29 years old"] >= 0.3 and (abs(image_age["60 years old or older"] - image_age["10~29 years old"]) < 0.2 or abs(image_age["31~59 years old"] - image_age["10~29 years old"])):
            image_age["10~29 years old"] = image_age["10~29 years old"] + image_age["60 years old or older"]/2
            image_age["10~29 years old"] = image_age["10~29 years old"] + image_age["31~59 years old"]/2
            image_age["60 years old or older"] /= 2
            image_age["31~59 years old"] /= 2

with open("/data/hanjun/test/explicit/finetuned_average_sdxl.json", "w") as f2:
    json.dump(data, f2, indent = 4)
f2.close()        
        