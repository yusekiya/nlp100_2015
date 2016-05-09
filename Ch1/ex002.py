# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
pat = 'パトカー'
taxi = 'タクシー'
ret = [pat[i] + taxi[i] for i in range(min(len(pat), len(taxi)))]
print("".join(ret))
