# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．
import ex041

def main():
    sentences = ex041.generate_chunks_whole_sentence()
    for sentence in sentences:
        for chunk in sentence:
            dst = chunk.dst
            if dst == -1: continue
            dst_chunk = sentence[dst]
            src_phrase = chunk.get_phrase()
            dst_phrase = dst_chunk.get_phrase()
            if src_phrase == '': continue
            print('{}\t{}'.format(src_phrase, dst_phrase))


if __name__ == '__main__':
    main()
