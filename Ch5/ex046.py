# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
# 45の仕様に加えて，以下の仕様を満たすようにせよ．
#
# - 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# - 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
import ex041

def main():
    sentences = ex041.generate_chunks_whole_sentence()
    for sentence in sentences:
        for chunk in sentence:
            verb_base = [m.base for m in chunk.morphs if m.pos=='動詞']
            if not verb_base: continue
            src_chunks = [sentence[i] for i in chunk.srcs]
            pp_surface_list = [(m.base, src_chunk.get_phrase()) for src_chunk in src_chunks
                               for m in src_chunk.morphs if m.pos=='助詞']
            if pp_surface_list:
                pp_surface_list = sorted(pp_surface_list, key=lambda x: x[0])
                pp_list, surface_list = zip(*pp_surface_list)
                print('{}\t{}\t{}'.format(verb_base[0], ' '.join(pp_list), ' '.join(surface_list)))


if __name__ == '__main__':
    main()
