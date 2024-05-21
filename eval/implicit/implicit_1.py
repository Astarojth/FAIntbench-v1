import json
from scipy.spatial.distance import cosine

def calculate_cosine_similarity(dict1, dict2):
    # Ensure both dictionaries have the same keys
    keys = set(dict1.keys()).intersection(set(dict2.keys()))
    if not keys:
        return 1.0  # If no common keys, cosine similarity is 1.0 (considered as completely different)

    vec1 = [dict1[key] for key in keys]
    vec2 = [dict2[key] for key in keys]
    return 1 - cosine(vec1, vec2)

def main():
    result = {}
    with open('/data/hanjun/test/implicit/average_sdxl.json', 'r', encoding='utf-8') as average:
        average_data = json.load(average)
    average.close()
    # calculate cosine similarity for occupation
    with open('/data/hanjun/truth/oc_gt.json', 'r', encoding='utf-8') as oc_gt, open('/data/hanjun/truth/char_gt.json', 'r', encoding='utf-8') as char_gt, open('/data/hanjun/truth/sr_gt.json', 'r', encoding='utf-8') as sr_gt:
        oc_gt_data = json.load(oc_gt)
        char_gt_data = json.load(char_gt)
        sr_gt_data = json.load(sr_gt)
    oc_gt.close()
    char_gt.close()
    sr_gt.close()

    for prompt in average_data:
        if prompt in oc_gt_data:
            result[prompt] = {}
            for attribute in ['gender', 'race', 'age']:
                if attribute in average_data[prompt] and attribute in oc_gt_data[prompt]:
                    similarity = calculate_cosine_similarity(average_data[prompt][attribute], oc_gt_data[prompt][attribute])
                    normalized_similarity = (similarity + 1) / 2
                    result[prompt][attribute] = similarity
        elif prompt in char_gt_data:
            result[prompt] = {}
            for attribute in ['gender', 'race', 'age']:
                if attribute in average_data[prompt] and attribute in char_gt_data[prompt]:
                    similarity = calculate_cosine_similarity(average_data[prompt][attribute], char_gt_data[prompt][attribute])
                    normalized_similarity = (similarity + 1) / 2
                    result[prompt][attribute] = similarity
        elif prompt in sr_gt_data:
            result[prompt] = {'left': {}, 'right': {}}
            for position in ['left', 'right']:
                for attribute in ['gender', 'race', 'age']:
                    if attribute in average_data[prompt][position] and attribute in sr_gt_data[prompt][position]:
                        similarity = calculate_cosine_similarity(average_data[prompt][position][attribute], sr_gt_data[prompt][position][attribute])
                        normalized_similarity = (similarity + 1) / 2
                        result[prompt][position][attribute] = similarity
     
    
    
    with open('cosine_similarity_results.json', 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)
    print("Cosine similarity results have been written to 'cosine_similarity_results.json'.")

if __name__ == "__main__":
    main()
