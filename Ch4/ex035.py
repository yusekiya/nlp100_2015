# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
import ex030

def extract_noun_sequence():
    result = ex030.morpheme_analysis()
    ret = set()
    for sentence in result:
        ns = []
        for m in sentence:
            if m['pos'] == '名詞':
                ns.append(m['surface'])
            else:
                if len(ns) > 1:
                    ret.add(''.join(ns))
                    ns = []
                else:
                    ns = []
        if len(ns) > 1: ret.add(''.join(ns))
    return ret


def main():
    print(extract_noun_sequence())


if __name__ == '__main__':
    main()
