import json

def process_and_update_json(input_filepath, output_filepath):
    # 读取json文件
    with open(input_filepath, 'r') as f:
        data = json.load(f)

    # 初始化一个新的字典来存储处理后的数据
    new_data = {}

    # 遍历data中的键，处理以"O"开头的键
    keys_to_delete = []
    for key in data:
        if key.startswith('O') and 'with' in key:
            # 分割key以获取新键名
            left_part, right_part = key.split(' with ')
            left_part = left_part.strip()
            right_part = right_part.strip()

            # 获取left和right的内容
            left_content = data[key].get('left', {})
            right_content = data[key].get('right', {})

            # 创建新的键并赋值
            new_data[left_part] = left_content
            new_data[right_part] = right_content

            # 记录需要删除的键
            keys_to_delete.append(key)

    # 删除原始数据中的旧键
    for key in keys_to_delete:
        del data[key]

    # 将新数据加入原始数据中
    data.update(new_data)

    explicit=["man", "woman", "young", "male", "female", "elderly", "middle-aged", "African", "East-Asian", "South-Asian", "European", "Latino"]
    # 删除所有键名中含有 "man", "woman", "young" 的键
    keys_to_delete = [key for key in data if any(substring in key for substring in explicit)]
    for key in keys_to_delete:
        del data[key]

    # 保存更新后的数据到输出文件
    with open(output_filepath, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Processing complete, results saved to '{output_filepath}'")

# 调用函数并处理JSON文件
process_and_update_json('average_sdxl.json', 'meta_eta.json')
