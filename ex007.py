# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
def ex7(x, y, z):
    string = '{}時の{}は{}'.format(x,y,z)
    return string

def main():
    x = 12
    y = '気温'
    z = '22.4'
    print(ex7(x,y,z))
    return 0

if __name__ == '__main__':
    main()
