# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．
import json
with open('jawiki-country.json') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            # print(data['text'])
            with open('UK.txt', 'w') as of:
                of.write(data['text'])
            break
print('finished')
