# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．
import re

def make_info_dict():
    # Regex pattern to extract infobox
    p_infobox = re.compile(r'^\{\{(基礎情報(?:[^\}]+?(?:\{\{.+?\}\})?)*)\}\}', re.MULTILINE | re.DOTALL)
    # Regex pattern to split infobox
    p_split = re.compile(r'(\|[^=\|]+=)', re.DOTALL)
    # Regex pattern to get keys
    p_key = re.compile(r'\|([^=]+)=')
    with open('UK.txt', 'r') as f:
        content = f.read()
    infobox = p_infobox.search(content).group(1)
    infobox_list = p_split.split(infobox)[1:]
    keys = [p_key.search(key).group(1).strip() for key in infobox_list[::2]]
    values = [value.strip() for value in infobox_list[1::2]]
    info_dict = dict(zip(keys, values))
    return info_dict


def main():
    print(make_info_dict())


if __name__ == '__main__':
    main()
