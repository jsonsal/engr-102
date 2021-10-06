board = [['A','B','C','D' ,'E','F','G','H'], [1,2,3,4,5,6,7,8]]

for i in range(len(board[0])):
    print(board[0][i].rjust(4), end='')
print("\n", end='')
for i in range(len(board[1])):
    print(board[1][i], '.')