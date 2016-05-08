# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
import re
pattern = re.compile(r'\[\[Category:(.+)\]\]')
with open('UK.txt', 'r') as f:
    for line in f:
        m = pattern.match(line.strip())
        if m:
            print(m.group(1))
