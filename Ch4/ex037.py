# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
import numpy as np
import ex036
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    params = {
        'font.family'   : 'Osaka',
        'font.size' : 20,
    }
    mpl.rcParams.update(params)

    wc = ex036.count_word()
    occurrence = ex036.sort_by_occurrence(wc, n=10)
    data = np.array(occurrence)
    label = data[:, 0].tolist()
    Y = data[:, 1].astype(int)
    X = np.arange(Y.shape[0])
    plt.bar(X, Y, align='center', width=0.8)
    plt.xlim(-0.5, 9.5)
    plt.xticks(X, label)
    plt.show()


if __name__ == '__main__':
    main()
