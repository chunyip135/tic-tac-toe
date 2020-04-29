#tic-tac-toe
#initial value / start value
iv = ['-', '-', '-',
      '-', '-', '-',
      '-', '-', '-',]

#board
def board():
  print(iv[0] + ' | ' + iv[1] + ' | ' + iv[2])
  print(iv[3] + ' | ' + iv[4] + ' | ' + iv[5])
  print(iv[6] + ' | ' + iv[7] + ' | ' + iv[8])

def play_game():
  board()
  i = 0
  number = [1,2,3,4,5,6,7,8,9]
  while i < 9:
    move = i + 1
    if move%2 !=0:
      index = int(input('Player 1 turns: '))
      if index in number:
        iv[index-1] = 'X'
      else:
        print('Number used, please enter another number :')
        index = int(input('Player 1 turns: '))
        iv[index-1] = 'X'
    else:
      index = int(input('Player 2 turns: '))
      if index in number:
        iv[index-1] = 'O'
      else:
        print('Number used, please enter another number :')
        index = int(input('Player 2 turns: '))
        iv[index-1] = 'O'
    number.remove(index)

    #test for all wining cases
    for k in [0,3,5]: #rows
      if iv[k:k+3] == ['X','X','X']:
        print('Player 1, X wins')
        i = 9
      elif iv[k:k+3] == ['O','O','O']:
        print('Player 2, O wins')
        i = 9
  
    for k in [0,1,2]: #columns
      if [iv[k], iv[k+3], iv[k+6]] == ['X','X','X']:
        print('Player 1, X wins')
        i = 9
      elif [iv[k], iv[k+3], iv[k+6]] == ['O','O','O']:
        print('Player 2, O wins')
        i = 9
    
    #oblique (left to right)
    if [iv[0], iv[4], iv[8]] == ['X','X','X']:
      print('Player 1, X wins')
      i = 9
    elif [iv[0], iv[4], iv[8]] == ['O','O','O']:
      print('Player 2, O wins')
      i = 9

    #oblique (right to left)
    if [iv[2], iv[4], iv[6]] == ['X','X','X']:
      print('Player 1, X wins')
      i = 9
    elif [iv[2], iv[4], iv[6]] == ['O','O','O']:
      print('Player 2, O wins')
      i = 9
    board()
    i += 1
  
play_game()