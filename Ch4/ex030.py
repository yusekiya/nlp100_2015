# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
# をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．
# 
# 形態素解析結果 format: 表層形,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
# あらかじめ sed コマンドでタブをカンマに置換しておく
def make_morpheme_dict(line):
    ml = line.split(',')
    return dict(surface=ml[0],
                base=ml[7],
                pos=ml[1],
                pos1=ml[2])


def morpheme_analysis():
    ret = []
    with open('neko.txt.mecab', 'r') as f:
        ms = []
        for fl in f:
            line = fl.rstrip()
            if not line == 'EOS':
                ms.append(make_morpheme_dict(line))
            else:
                if len(ms) > 0:
                    ret.append(ms)
                    ms = []
    return ret


def main():
    result = morpheme_analysis()
    print('Show some results')
    print(result[:4])


if __name__ == '__main__':
    main()
