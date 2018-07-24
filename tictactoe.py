cnt=0
def read_player_name_choice(n):
   inp=input("Name, ch='X/O' and First=Y/N for player {}:".format(n))
   inp_list=inp.split(",")
   return tuple(inp_list)
def check_row():
   for i in range(3):
       if board[(i,0)]+board[(i,1)]+board[(i,2)]=="OOO":
           return True,'O'
       if board[(i,0)]+board[(i,1)]+board[(i,2)]=="XXX":
           return True,'X'
   return (False," ")
def check_cols():
   for i in range(3):
       if board[(0,i)]+board[(1,i)]+board[(2,i)]=="OOO":
           return (True,'O')
       if board[(0,i)]+board[(1,i)]+board[(2,i)]=="XXX":
           return (True,'X')
   return (False," ")
def check_diag():
   #print([(0,0)],board[(1,1)],board[(2,2)])
   if board[(0,0)]+board[(1,1)]+board[(2,2)]=="OOO":
       return (True,'O')
   if board[(2,0)]+board[(1,1)]+board[(0,2)]=="OOO":
       return (True,'O')
   if board[(0,0)]+board[(1,1)]+board[(2,2)]=="XXX":
       return (True,'X')
   if board[(2,0)]+board[(1,1)]+board[(0,2)]=="XXX":
       return (True,'X')
   return (False," ")

def check_winner():
   winner=False
   ch="A"
   for i in range(3):
       winner,ch=check_row()
       if not winner:
           winner,ch=check_cols()
       if not winner:
           winner,ch=check_diag()
       if winner:
           break
   if players[player][1]==ch:
       print ("Winner is {}".format(players[player][0]))
   if players[1-player][1]==ch:
       print ("Winner is {}".format(players[1-player][0]))
   print_board()
   return winner
       
       
           
def get_input(player):
   global cnt
   cnt+=1
   pos=input("Please give position as cordinate(0,1):").strip().split(",")
   if pos=='q':
       raise Exception('Failing tictactoe!')
   pos=tuple([int(i) for i in pos])
   player=1-player
   board[pos]=players[player][1]
   #print(pos,players)
   return player
   
def is_valid_position(pos):
   valid=False
   for i in board:
       if pos==i:
           valid=True
   return valid

def print_board():
   brd=""
   for i in range(3):
       for j in range(3):
           if j==2:
               brd=brd+"|"+board[(i,j)]+"|\n_______\n"
           else:
               brd=brd+"|"+board[(i,j)]
   print(brd)
players={}
player=1
board={(0,0): " ",(0,1):" ", (0,2):" ",
      (1,0): " ",(1,1):" ", (1,2):" ",
      (2,0): " ",(2,1):" ", (2,2):" ",
      }
print_board()


for i in range(2):
   players[i]=read_player_name_choice(1)
   print(players[i])
while True:
   player=get_input(player)
   if check_winner():
       break
   if cnt==9:
       print("Its stalemate")
       break
   