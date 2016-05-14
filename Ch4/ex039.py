# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
import ex036
import matplotlib.pyplot as plt
import numpy as np

def main():
    wc = ex036.count_word()
    occurrence = ex036.sort_by_occurrence(wc)
    data = np.array(occurrence)
    data = data[:, 1].astype(int)
    X = np.arange(data.shape[0])
    plt.loglog(X, data, 'o')
    plt.show()


if __name__ == '__main__':
    main()
