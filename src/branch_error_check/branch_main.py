import os
import json


# 获取语言文件，处理得到一个 dict
def lang_to_dict(file_path):
    lang_dict = {}
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            if line is not None and line[0] != '#' and line[0] != '/' and '=' in line:
                line_list = line.split('=', 1)
                lang_dict[line_list[0]] = line_list[1].rstrip('\n')
    return lang_dict


def file_finder(assets_path):
    return [
        modid
        for modid in os.listdir(assets_path)
        if os.path.isfile(f'{assets_path}/{modid}/lang/en_us.lang')
        and os.path.isfile(f'{assets_path}/{modid}/lang/zh_cn.lang')
    ]


def main_check(zh_dict_in, modid_in):
    return [
        {'modid': modid_in, 'key': k, 'zh_cn': zh_dict_in[k]}
        for k in zh_dict_in.keys()
        if '=' in zh_dict_in[k] and '.' in zh_dict_in[k]
    ]


def branch_check(path):
    list_total_in = []
    for modid in file_finder(path):
        list_total_in.extend(
            main_check(lang_to_dict(f'{path}/{modid}/lang/zh_cn.lang'), modid)
        )

    return json.dumps(list_total_in, ensure_ascii=False)


if __name__ == '__main__':
    list_total = []

    for modid in file_finder('../project/assets'):
        zh_dict = lang_to_dict(f'../project/assets/{modid}/lang/zh_cn.lang')
        list_total.extend(main_check(zh_dict, modid))

    print(json.dumps(list_total, ensure_ascii=False))
