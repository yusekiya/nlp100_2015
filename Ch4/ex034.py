# 2つの名詞が「の」で連結されている名詞句を抽出せよ．
# 「の」は助詞,連体化
import ex030

def extract_noun_phrase():
    result = ex030.morpheme_analysis()
    ret = set()
    for sentence in result:
        pos1_list = [mopheme['pos1'] for mopheme in sentence]
        adnomial_ind = (index for index, string in enumerate(pos1_list) if string == '連体化')
        for i in adnomial_ind:
            try:
                mb = sentence[i-1]
                ma = sentence[i+1]
                if (mb['pos'] == '名詞' and ma['pos'] == '名詞'):
                    noun_phrase = sentence[i-1]['surface'] + 'の' + sentence[i+1]['surface']
                    ret.add(noun_phrase)
            except IndexError:
                pass
    return ret


def main():
    print(extract_noun_phrase())


if __name__ == '__main__':
    main()
