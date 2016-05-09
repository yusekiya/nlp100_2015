# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．
import pandas as pd
col1 = pd.read_csv('col1.txt', header=None, index_col=False)
print(col1[0].value_counts())
