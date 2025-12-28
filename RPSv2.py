import random 

#moves store
moves=["r","p","s"]  
moves_fname={"r":"Rock",
            "s":"Scissor",
            "p":"Paper"}
computer_point=0
user_point=0 

#computer random roll
def computer_move():
  move=random.choice(moves)
  return move

def show_n_call( user_move, c_move, won):
  global user_point
  global computer_point
  print(f"""Your move:{moves_fname[user_move]}
Opponent move:{moves_fname[c_move]}""")
#decides win/lose/draw
  if won=="y":
    print("You won!")
    user_point+=1
  elif won=="n":
    print("You lost!")
    computer_point+=1
    #gives both user and computer a point
  else:
    print("Draw!")
    computer_point+=1
    user_point+=1
  print(f"""Your point:{user_point}
opponent point:{computer_point}""")
#asks for play again 
  u_choice=str(input("Do you want to play again?(Y/N): "))
  while u_choice.lower()!="y" and u_choice.lower()!="n":
      print("Please enter a valid choice!")
      u_choice=str(input("Do you want to play again?(Y/N): ")) 
  return u_choice



print("""● Welcome to Rock Paper Scissor Game.
Shall we play? (Y/N):""") 
#gets user choice
user_choice=str(input(" "))

while user_choice.lower()=="y":
  print("""■ Pick move -Rock(R),Paper(P),Scissor(S)-""")
  user_move=(str(input(": "))).lower()
  c_move=computer_move()
  #Checks if it is a valid move
  while user_move!="r" and user_move!="s" and user_move!="p":
    print("invalid choice")
    user_move=(str(input("Enter move: "))).lower() 
  #win
  if (user_move.lower()=="r" and c_move=="s") or (user_move.lower()=="s" and c_move=="p") or (user_move.lower()=="p" and c_move=="r"):
    user_choice=show_n_call(user_move, c_move, "y")
   #lose
  elif (user_move.lower()=="s" and c_move=="r") or (user_move.lower()=="p" and c_move=="s") or (user_move.lower()=="r" and c_move=="p"):
    user_choice=show_n_call( user_move, c_move, "n")

  #draw
  elif user_move==c_move:
    user_choice=show_n_call( user_move, c_move, "d")


      
    
      

  