# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．
import ex041

def main():
    sentences = ex041.generate_chunks_whole_sentence()
    for sentence in sentences:
        for chunk in sentence:
            dst = chunk.dst
            if dst == -1: continue
            dst_chunk = sentence[dst]
            if chunk.has_noun() and dst_chunk.has_verb():
                src_phrase = chunk.get_phrase()
                dst_phrase = dst_chunk.get_phrase()
                assert src_phrase != '', 'Source phrase is empty'
                print('{}\t{}'.format(src_phrase, dst_phrase))


if __name__ == '__main__':
    main()
