# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
import sys
N = int(sys.argv[1])
with open('hightemp.txt', 'r') as f:
    lines = f.readlines()
    nl = len(lines)
    q, r = divmod(nl, N)
    ind = 0
    for i in range(r):
        ind += 1
        print('Chunk{}:'.format(ind))
        bs = q + 1
        print(''.join(lines[bs*i:bs*(i+1)]))
    for i in range(N-r):
        ind += 1
        print('Chunk{}:'.format(ind))
        bs = q
        lines = lines[(q+1)*r:]
        print(''.join(lines[bs*i:bs*(i+1)]))
