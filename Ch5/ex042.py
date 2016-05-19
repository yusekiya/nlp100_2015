# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．
import ex041

def main():
    chunks = ex041.generate_chunks_whole_sentence()
    for sentence in chunks:
        res = []
        for chunk in sentence:
            surfaces = [m.surface for m in chunk.morphs if m.pos != '記号']
            dst = chunk.dst
            res.append((''.join(surfaces), dst))
        for surface, dst in res:
            if dst != -1:
                surface_dst = res[dst][0]
            else:
                surface_dst = 'None'
            if surface != '':
                print('{}\t{}'.format(surface, surface_dst))


if __name__ == '__main__':
    main()
