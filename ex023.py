# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
import re
pattern = re.compile(r'=+(.+?)(=+)=')
with open('UK.txt', 'r') as f:
    for line in f:
        m = pattern.match(line.strip())
        if m:
            print(m.group(1).strip(), len(m.group(2)))
