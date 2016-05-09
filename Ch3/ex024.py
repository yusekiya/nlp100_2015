# 記事から参照されているメディアファイルをすべて抜き出せ．
import re
pattern_file_obj = re.compile(r'\[\[File:([^|]+).*\]\]')
with open('UK.txt', 'r') as f:
    for line in f:
        mf = pattern_file_obj.findall(line.strip())
        if mf:
            for m in mf:
                print(m.strip().replace(' ', '_'))
