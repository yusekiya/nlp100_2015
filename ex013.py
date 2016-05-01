# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と
# 2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
import pandas as pd

col1 = pd.read_csv('col1.txt', header=None, index_col=False)
col2 = pd.read_csv('col2.txt', header=None, index_col=False)
col12 = pd.concat([col1, col2], axis=1)
col12.to_csv('col12.txt', index=False, header=False, sep=' ')
