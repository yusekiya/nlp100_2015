# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
from ex005 import create_n_gram
str1 = 'paraparaparadise'
str2 = 'paragraph'
bg1 = create_n_gram(str1, 2)
bg2 = create_n_gram(str2, 2)

X = set(bg1)
print('X: ', end='')
print(X)
Y = set(bg2)
print('Y: ', end='')
print(Y)
print()
print('Union')
print(X|Y)
print()
print('Intersection')
print(X&Y)
print()
print('X-Y')
print(X-Y)
print()
print('Y-X')
print(Y-X)
print()
if 'se' in X:
    print('\'se\' is included in X')
else:
    pass
if 'se' in Y:
    print('\'se\' is included in Y')
else:
    pass
