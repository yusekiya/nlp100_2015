# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
import re
# Regex pattern to extract infobox
p_infobox = re.compile(r'^\{\{(基礎情報(?:[^\}]+?(?:\{\{.+?\}\})?)*)\}\}', re.MULTILINE | re.DOTALL)
# Regex pattern to split infobox
p_split = re.compile(r'(\|[^=\|]+=)', re.DOTALL)
# Regex pattern to get keys
p_key = re.compile(r'\|([^=]+)=')
# Regex pattern for emphasis
p_emph = re.compile(r'\'{2,5}')
# Regex pattern for link to another page
p_link_to_wiki = re.compile(r'\[\[(?:[^:\]]+\|)?([^:]*?)\]\]')


def make_info_dict_without_emph_nor_link():
    with open('UK.txt', 'r') as f:
        content = f.read()
    infobox = p_infobox.search(content).group(1)
    infobox_list = p_split.split(infobox)[1:]
    keys = [p_key.search(key).group(1).strip() for key in infobox_list[::2]]
    values = [remove_markup(value.strip()) for value in infobox_list[1::2]]
    info_dict = dict(zip(keys, values))
    return info_dict


def remove_markup(string):
    # Remove emphasis
    ret = p_emph.sub('', string)
    # Remove link to another page
    ret = p_link_to_wiki.sub(r'\1', ret)
    return ret


def main():
    print(make_info_dict_without_emph_nor_link())


if __name__ == '__main__':
    main()
