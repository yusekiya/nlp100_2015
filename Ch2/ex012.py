# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．
import pandas as pd

df = pd.read_table('hightemp.txt', header=None, names=['都道府県', '地点', '気温', '日付'],
                   index_col=False, delim_whitespace=True)
df.iloc[:, 0].to_csv('col1.txt', index=False)
df.iloc[:, 1].to_csv('col2.txt', index=False)
