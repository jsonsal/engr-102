board = [['A','B','C','D' ,'E','F','G','H'], [1,2,3,4,5,6,7,8]]

for i in range(len(board[0])):
    print(board[0][i].rjust(4), end='')
print("\n", end='')
aone = str(board[1][0]) + str('  .')
atwo = str(board[1][1]) + str('  .')
athree = str(board[1][2]) + str('  .')
afour = str(board[1][3]) + str('  .')
afive = str(board[1][4]) + str('  .')
asix = str(board[1][5]) + str('  .')
aseven = str(board[1][6]) + str('  .')
aeight = str(board[1][7]) + str('  .')
bone = str(board[0][0]) + str('  .')

print(aone)
print(atwo)
print(athree)
print(afour)
print(afive)
print(asix)
print(aseven)
print(aeight)
print(bone)