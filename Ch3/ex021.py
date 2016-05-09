# 記事中でカテゴリ名を宣言している行を抽出せよ．
with open('UK.txt', 'r') as f:
    for line in f:
        if ('Category:' in line):
            print(line.strip())
