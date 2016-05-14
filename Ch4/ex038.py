# 単語の出現頻度のヒストグラム
# （横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
import ex036
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def main():
    wc = ex036.count_word()
    occurrence = ex036.sort_by_occurrence(wc)
    data = np.array(occurrence)
    data = data[:, 1].astype(int)
    plt.yscale('log')
    plt.hist(data, bins=100)
    plt.show()


if __name__ == '__main__':
    main()
