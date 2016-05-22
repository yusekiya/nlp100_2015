# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．
import ex041

def main():
    chunks = ex041.generate_chunks_whole_sentence()
    for sentence in chunks:
        res = []
        for chunk in sentence:
            surfaces = [m.surface for m in chunk.morphs if m.pos != '記号']
            poses = [m.pos for m in chunk.morphs if m.pos != '記号']
            dst = chunk.dst
            res.append((''.join(surfaces), poses, dst))
        for surface, poses, dst in res:
            if surface == '':
                continue
            elif dst != -1 and '名詞' in poses and '動詞' in res[dst][1]:
                print('{}\t{}'.format(surface, res[dst][0]))
                surface_dst = res[dst][0]
            else:
                pass


if __name__ == '__main__':
    main()
