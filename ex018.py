# 各行を3コラム目の数値の逆順で整列せよ （注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
import pandas as pd
df = pd.read_table('hightemp.txt', header=None, names=['都道府県', '地点', '気温', '日付'],
                   index_col=False, delim_whitespace=True)
print(df.sort_values('気温', ascending=False))
