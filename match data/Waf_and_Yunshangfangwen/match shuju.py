import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f.readlines()]

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def match_json_data(file1_data, file2_data, field1, field2):
    matched_data = []

    file2_dict = {}
    for item in file2_data:
        key = (item[field1],item[field2])
        if key not in file2_dict:
            file2_dict[key] = []
        file2_dict[key].append(item)

    for item1 in file1_data:
        key = (item1[field1], item1[field2])
        if key in file2_dict:
            result = {"WAF日志":item1,"云上访问日志":[]}
            for matched_item in file2_dict[key]:
                result["云上访问日志"].append(matched_item)

            matched_data.append(result)

    return matched_data

file1_data = load_json('C:/Users/赵豪/Desktop/工作/数据中心/可研所需资料/外网相关文件/外网云上WAF日志/2024-12-12-16-49-53_RequestLogDetail.json')
file2_data = load_json('C:/Users/赵豪/Desktop/工作/数据中心/可研所需资料/外网相关文件/外网云上访问日志-12.09.7.00-8.30.59/2024-12-12-14-51-17_FullAccessLogDetail.json')

field1 = 'src_ip'
field2 = 'dest_ip'

matched_data = match_json_data(file1_data, file2_data, field1, field2)

save_json(matched_data, 'output.json')
