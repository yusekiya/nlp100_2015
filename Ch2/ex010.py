# 行数をカウントせよ．確認にはwcコマンドを用いよ．
import pandas as pd

df = pd.read_table('hightemp.txt', header=None, names=['都道府県', '地点', '気温', '日付'],
                   index_col=False, delim_whitespace=True)
print(df.shape[0])
