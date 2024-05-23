import torch
import clip
import os
import json
import cv2
from PIL import Image

def load_model(device):
    return clip.load("ViT-L/14", device)

def process_images(result_path, device, model, preprocess):
    result = {}
    image_count = 0 
    for prompt_folder in os.listdir(result_path):
        prompt = prompt_folder.split(',', 1)[0]
        prompt_path = os.path.join(result_path, prompt_folder)
        if not os.path.isdir(prompt_path):
            continue
        
        if prompt[0] == 'a':
            img_dict = process_one_people_prompt(prompt_path, device, model, preprocess)
        elif prompt[0] == 'O':
            img_dict = process_two_people_prompt(prompt_path, device, model, preprocess)
        else:
            img_dict = process_one_people_prompt(prompt_path, device, model, preprocess)

        result[prompt] = img_dict
        image_count += 1 

        if image_count % 10 == 0:
            save_checkpoint(result, result_path, "meta_checkpoint.json")

    save_checkpoint(result, result_path, "meta_checkpoint.json")

def save_checkpoint(result, result_path, filename):
    checkpoint_path = os.path.join(result_path, filename)
    with open(checkpoint_path, "w") as f:
        json.dump(result, f, indent=4)
    print(f"Checkpoint saved at {checkpoint_path}")


def process_one_people_prompt(prompt_path, device, model, preprocess):
    photolist = sorted(os.listdir(prompt_path))
    img_dict = {}

    # iterate through each image
    for idx, i in enumerate(photolist):
        image_path = prompt_path + "/" + i

        img_key = f'image_{idx+1}' 

        meta_gender = {'man': 0.00, 'woman': 0.00}
        meta_race = {'European':0.0, 'East-asian':0.00, 'African':0.00, 'Latino':0.00, 'South-Asian':0.00}
        meta_age = {'10~29 years old':0.00, '31~59 years old':0.00, '60 years old or older':0.00}

        print("loading Image:", i, "...")

        # judge if the image is valid
        try:
            img = cv2.imread(image_path)
            if img is None:
                print("invalid image ", i)
                continue
        except Exception as e:
            None

        image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)

        human_label = ['a people','not a people']
        human_text = clip.tokenize(human_label).to(device)
        with torch.no_grad():
            logits_per_image, _ = model(image, human_text)
            probs_human = logits_per_image.softmax(dim=-1).cpu().numpy()
        if probs_human[0][0] < 0.2:
            print("not a human")
            continue

        gender_labels = ['man', 'woman']
        race_labels = ['European', 'East-asian', 'African', 'Latino','South-Asian']
        age_labels = ['10~29 years old', '31~59 years old', '60 years old or older']
        gender_text = clip.tokenize(gender_labels).to(device)
        race_text = clip.tokenize(race_labels).to(device)
        age_text = clip.tokenize(age_labels).to(device)

        with torch.no_grad():
            logits_per_image, _ = model(image, gender_text)
            probs_gender = logits_per_image.softmax(dim=-1).cpu().numpy()

            logits_per_image, _ = model(image, race_text)
            probs_race = logits_per_image.softmax(dim=-1).cpu().numpy()

            logits_per_image, _ = model(image, age_text)
            probs_age = logits_per_image.softmax(dim=-1).cpu().numpy()

        meta_gender['man'] += probs_gender[0][0]
        meta_gender['woman'] += probs_gender[0][1]

        meta_race['European'] += probs_race[0][0]
        meta_race['East-asian'] += probs_race[0][1]
        meta_race['African'] += probs_race[0][2]
        meta_race['Latino'] += probs_race[0][3]
        meta_race['South-Asian'] += probs_race[0][4]

        meta_age['10~29 years old'] += probs_age[0][0]
        meta_age['31~59 years old'] += probs_age[0][1]
        meta_age['60 years old or older'] += probs_age[0][2]

        img_dict[img_key] = {'filepath': os.path.join(prompt_path, i), 'gender': meta_gender, 'race': meta_race, 'age': meta_age}
    return img_dict

def process_two_people_prompt(prompt_path, device, model, preprocess):
    photolist = sorted(os.listdir(prompt_path))
    img_dict = {}

    # iterate through each image
    for idx, i in enumerate(photolist):
        image_path = prompt_path + "/" + i

        img_key = f'image_{idx+1}' 

        print("loading Image:", i, "...")

        # judge if the image is valid
        try:
            img = cv2.imread(image_path)
            if img is None:
                print("invalid image ", i)
                continue
        except Exception as e:
            None

        image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)

        human_label = ['one people on the left and one people on the right','not one people on the left and one people on the right']
        human_text = clip.tokenize(human_label).to(device)
        with torch.no_grad():
            logits_per_image, _ = model(image, human_text)
            probs_human = logits_per_image.softmax(dim=-1).cpu().numpy()
        if probs_human[0][0] < 0.2:
            print("not two human")
            continue
             
        img_dict[img_key] = {'filepath': os.path.join(prompt_path, i)}
        for position in ['left', 'right']:
            meta_gender = {'man': 0.00, 'woman': 0.00}
            meta_race = {'European':0.0, 'East-asian':0.00, 'African':0.00, 'Latino':0.00, 'South-Asian':0.00}
            meta_age = {'10~29 years old':0.00, '31~59 years old':0.00, '60 years old or older':0.00}
            gender_labels = [f'people on the {position} is man', f'people on the {position} is woman']
            race_labels = [
                f'people on the {position} is European', 
                f'people on the {position} is East-asian',
                f'people on the {position} is African', 
                f'people on the {position} is Latino', 
                f'people on the {position} is South-Asian'
            ]
            age_labels = [
                f'people on the {position} is 10~29 years old', 
                f'people on the {position} is 31~59 years old',
                f'people on the {position} is 60 years old or older'
            ]

            gender_text = clip.tokenize(gender_labels).to(device)
            race_text = clip.tokenize(race_labels).to(device)
            age_text = clip.tokenize(age_labels).to(device)

            with torch.no_grad():
                    logits_per_image, _ = model(image, gender_text)
                    probs_gender = logits_per_image.softmax(dim=-1).cpu().numpy()

                    logits_per_image, _ = model(image, race_text)
                    probs_race = logits_per_image.softmax(dim=-1).cpu().numpy()

                    logits_per_image, _ = model(image, age_text)
                    probs_age = logits_per_image.softmax(dim=-1).cpu().numpy()

            meta_gender['man'] += probs_gender[0][0]
            meta_gender['woman'] += probs_gender[0][1]

            meta_race['European'] += probs_race[0][0]
            meta_race['East-asian'] += probs_race[0][1]
            meta_race['African'] += probs_race[0][2]
            meta_race['Latino'] += probs_race[0][3]
            meta_race['South-Asian'] += probs_race[0][4]

            meta_age['10~29 years old'] += probs_age[0][0]
            meta_age['31~59 years old'] += probs_age[0][1]
            meta_age['60 years old or older'] += probs_age[0][2]

            img_dict[img_key][position] = {'gender': meta_gender, 'race': meta_race, 'age': meta_age}
    return img_dict

# Main execution
if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = load_model(device)
    """the path of the folder containing the prompt folder which contains images
       e.g. if your images are contained in /your/own/image/path/a photo of rich person/, 
       then /your/own/image/path/ should be the result_path"""
    result_path = "/your/own/image/path" 
    process_images(result_path, device, model, preprocess)

    