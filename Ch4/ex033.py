# サ変接続の名詞をすべて抽出せよ．
import ex030

def main():
    result = ex030.morpheme_analysis()
    ret = set()
    for sentence in result:
        for mopheme in sentence:
            if mopheme['pos1'] == 'サ変接続':
                ret.add(mopheme['base'])
    print(ret)


if __name__ == '__main__':
    main()
