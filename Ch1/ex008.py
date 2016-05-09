# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#    - 英小文字ならば(219 - 文字コード)の文字に置換
#    - その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
def cipher(s):
    enc = [chr(219-ord(c)) if c.islower() else c for c in s]
    return ''.join(enc)

def main():    
    orig = 'I couldn\'t believe that I could actually understand '\
           'what I was reading: the phenomenal power of the human mind.'
    print('original: {}'.format(orig))
    print()
    encoded = cipher(orig)
    print('encoded: {}'.format(encoded))
    print()
    decoded = cipher(encoded)
    print('decoded: {}'.format(decoded))

if __name__ == '__main__':
    main()
