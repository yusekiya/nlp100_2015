# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．
import pandas as pd

col1 = pd.read_csv('col1.txt', header=None, index_col=False)
print(col1.drop_duplicates())
