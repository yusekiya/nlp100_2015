# 動詞の表層形をすべて抽出せよ．
import ex030

def main():
    result = ex030.morpheme_analysis()
    ret = set()
    for sentence in result:
        for mopheme in sentence:
            if mopheme['pos'] == '動詞':
                ret.add(mopheme['surface'])
    print('{} verbs found:'.format(len(ret)))
    print(ret)
kkkkkkkkkkkkkkk

if __name__ == '__main__':
    main()
