# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
# 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
# ただし，出力は以下の仕様を満たすようにせよ．
#
#     - 動詞を含む文節において，最左の動詞の基本形を述語とする
#     - 述語に係る助詞を格とする
#     - 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
import ex041

def main():
    sentences = ex041.generate_chunks_whole_sentence()
    for sentence in sentences:
        for chunk in sentence:
            verb_base = [m.base for m in chunk.morphs if m.pos == '動詞']
            if not verb_base: continue
            src_chunks = [sentence[i] for i in chunk.srcs]
            pp_list = [m.base for src_chunk in src_chunks for m in src_chunk.morphs if m.pos=='助詞']
            if pp_list: print('{}\t{}'.format(verb_base[0], ' '.join(pp_list)))


if __name__ == '__main__':
    main()
