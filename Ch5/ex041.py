# 40に加えて，文節を表すクラスChunkを実装せよ．
# このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
# 係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
# さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
# 8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
from ex040 import Morph, extract_morph_data
import re

p_dependency = re.compile(r'\*\s(\d+)\s(-?\d+)D')

class Chunk(object):
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs


def dependency_analysis(sentence):
    dependency_data = [l for l in sentence if l.startswith('* ')]
    dependency = []
    for l in dependency_data:
        m = p_dependency.match(l)
        if m:
            dependency.append((int(m.group(1)), int(m.group(2))))
    return dependency


def morpheme_analysis(sentence):
    ret = []
    chunk = []
    for l in sentence:
        if l.startswith('* '):
            if len(chunk) > 0: ret.append(chunk)
            chunk = []
            continue
        else:
            chunk.append(Morph(*extract_morph_data(l)))
    if len(chunk) > 0: ret.append(chunk)
    return ret


def generate_chunks_for_sentence(sentence):
    chunk_list = []
    dependency = dependency_analysis(sentence)
    morph_sentence = morpheme_analysis(sentence)
    assert len(dependency) == len(morph_sentence), 'Mismatch of the number of chunks'
    for index, morphs in enumerate(morph_sentence):
        dst = dependency[index][1]
        srcs = [depen[0] for depen in dependency if depen[1] == index]
        chunk_list.append(Chunk(morphs, dst, srcs))
    return chunk_list


def generate_chunks_whole_sentence():
    ret = []
    with open('./neko.txt.cabocha', 'r') as f:
        sentence = []
        line = f.readline().rstrip()
        while line:
            if not line == 'EOS':
                sentence.append(line)
            else:
                if len(sentence) > 0:
                    ret.append(generate_chunks_for_sentence(sentence))
                sentence = []
            line = f.readline().rstrip()
    return ret


def main():
    chunks = generate_chunks_whole_sentence()
    res = []
    for chunk in chunks[6]:
        surfaces = [m.surface for m in chunk.morphs]
        dst = chunk.dst
        res.append((''.join(surfaces), dst))
    for surface, dst in res:
        if dst != -1:
            surface_dst = res[dst][0]
        else:
            surface_dst = 'None'
        print('{:　<12s} -> {}'.format(surface, surface_dst))
    return 0


if __name__ == '__main__':
    main()
    print('finished')
