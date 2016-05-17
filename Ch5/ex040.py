# 形態素を表すクラスMorphを実装せよ．
# このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
# さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，
# 3文目の形態素列を表示せよ．
#
# cabocha出力ファイル format: 表層形,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
# あらかじめ sed コマンドでタブをカンマに置換しておく
class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '表層形: {}, 基本形: {}, 品詞: {}, 品詞細分類1: {}'\
            .format(self.surface, self.base, self.pos, self.pos1)


def extract_morph_data(line):
    m = line.split(',')
    return [m[0], m[7], m[1], m[2]]


def dependency_analysis():
    ret = []
    with open('neko.txt.cabocha', 'r') as f:
        ml = []
        for fl in f:
            if fl.startswith('*'): continue
            line = fl.rstrip()
            if not line == 'EOS':
                ml.append(Morph(*extract_morph_data(line)))
            else:
                if len(ml) > 0:
                    ret.append(ml)
                    ml = []
                else:
                    pass
    return ret
            

def main():
    morpheme_list = dependency_analysis()
    for m in morpheme_list[2]:
        print(m)


if __name__ == '__main__':
    main()
