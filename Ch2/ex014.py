# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
import sys
N = int(sys.argv[1])
with open('hightemp.txt', 'r') as f:
    for i in range(N):
        print(f.readline(), end='')
