# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
import ex030
from collections import Counter

def count_word():
    result = ex030.morpheme_analysis()
    word_list = []
    for sentence in result:
        for m in sentence:
            word_list.append(m['base'])
    return Counter(word_list)


def sort_by_occurrence(word_counter, n=None):
    sorted_list = word_counter.most_common(n)
    return sorted_list


def main():
    wc = count_word()
    sl = sort_by_occurrence(wc)
    print(sl)


if __name__ == '__main__':
    main()
