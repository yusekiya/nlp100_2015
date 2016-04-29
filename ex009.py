# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading:
# the phenomenal power of the human mind."）を与え，その実行結果を確認せよ．
from random import sample

def shuffle_word(w):
    length = len(w)
    ret = w if length <= 4 else w[0] + ''.join(sample(w[1:-1], length-2)) + w[-1]
    return ret


def shuffle(s):
    words = s.split()
    shuffled_list = [shuffle_word(w) for w in words]
    return ' '.join(shuffled_list)
        
def main():
    sample = 'I couldn\'t believe that I could actually understand '\
             'what I was reading: the phenomenal power of the human mind.'
    print('original:')
    print(sample)
    print()
    print('shuffled:')
    print(shuffle(sample))

if __name__ == '__main__':
    main()
