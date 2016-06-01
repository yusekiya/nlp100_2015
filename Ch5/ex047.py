# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
# 46のプログラムを以下の仕様を満たすように改変せよ．
#
# - 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# - 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# - 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# - 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
import ex041

def main():
    sentences = ex041.generate_chunks_whole_sentence()
    for sentence in sentences:
        for ind, chunk in enumerate(sentence):
            if not (len(chunk.morphs) == 2 and
                    chunk.morphs[0].pos == '名詞' and
                    chunk.morphs[0].pos1 == 'サ変接続' and
                    chunk.morphs[1].pos == '助詞' and
                    chunk.morphs[1].base == 'を' and
                    sentence[chunk.dst].has_pos('動詞')): continue
            chunk_verb = sentence[chunk.dst]
            verb = [m.base for m in chunk_verb.morphs if m.pos=='動詞'][0]
            verb_block = chunk.get_phrase() + verb
            srcs_cn = chunk.srcs
            srcs_cv = chunk_verb.srcs
            srcs = set(srcs_cn).union(srcs_cv)
            src_chunks = [sentence[i] for i in srcs]
            pp_surface_list = [(m.base, src_chunk.get_phrase()) for src_chunk in src_chunks
                               for m in src_chunk.morphs if m.pos=='助詞']
            if pp_surface_list:
                pp_surface_list = sorted(pp_surface_list, key=lambda x: x[0])
                pp_list, surface_list = zip(*pp_surface_list)
                print('{}\t{}\t{}'.format(verb_block, ' '.join(pp_list), ' '.join(surface_list)))


if __name__ == '__main__':
    main()
