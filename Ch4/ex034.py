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
                mb = sentence[i-1:0:-1]
                noun_b = []
                for m in mb:
                    if m['pos'] == '名詞':
                        noun_b.append(m['surface'])
                    else:
                        break
                if len(noun_b) == 0: continue
                ma = sentence[i+1:]
                noun_a = []
                for m in ma:
                    if m['pos'] == '名詞':
                        noun_a.append(m['surface'])
                    else:
                        break
                if len(noun_a) == 0: continue
                noun_phrase = ''.join(noun_b[::-1]) + 'の' + ''.join(noun_a)
                ret.add(noun_phrase)
            except IndexError:
                pass
    return ret


def main():
    print(extract_noun_phrase())


if __name__ == '__main__':
    main()
