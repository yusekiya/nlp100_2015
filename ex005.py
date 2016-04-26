# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"i am an nlper"という文から単語bi-gram，文字bi-gramを得よ．
def create_n_gram(l, n):
    '''Return n-gram from list-like object.

    Parameters
    ----------
    l : array_like
        String or list of words

    n : int
        Order of n-gram

    Returns
    -------
    ngram : list of str
        N-gram of `l`

    '''
    length = len(l) - n
    ngram = [l[i:i+n] for i in range(length + 1)]
    return ngram

string = 'i am an nlper'
word_list = string.split()
print('Word-wise bi-gram:')
print(create_n_gram(word_list, 2))
print()
string_without_space = string.replace(' ', '')
print('Character-wise bi-gram:')
print(create_n_gram(string_without_space, 2))
