# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
import sys
N = int(sys.argv[1])
with open('hightemp.txt', 'r') as f:
    lines = f.readlines()
    nl = len(lines)
    assert nl > N, 'Too big integer input'
    for i in range(N):
        print(lines[i-N], end='')
