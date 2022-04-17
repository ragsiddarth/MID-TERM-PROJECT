#****************************************************************
#Name: Balijepalli Rag Sai Siddarth
#Student Number: A00233374
#
#ANA1001 Mid Term Project
#****************************************************************


#Important imports and list and creating variables
import time
import sys 


health = 100
coins = []
inventory = []
#Welcoming the USER 
user_name = input("Please enter your name :\n")
print("Welcome to Jack's Lantern")
time.sleep(4)
print("THIS GAME IS ABOUT A ESCAPE ROOM. THE CONCEPT OF JACK'S LANTERN IS JUST LIKE THE CONCEPT OF THE ESCAPE ROOM WHICH IS YOU WILL FIND THE CLUES AND YOU NEED TO CRACK THOSE CLUES IN ORDER TO GET OUT OF THE ROOM. IF YOU GET OUT OF THE ROOM, YOU WIN!!  ")

time.sleep(3)
print("BUT THIS IS NOT JUST A ESCAPE ROOM. THIS IS A HOUSE WHICH IS CALLED AS JACK'S LANTERN.")
print("\n...")
time.sleep(2)

print(f"\n{user_name.title()}, you are bored in your life and want to do something interesting and adventrous. One day you find a pamphlet in your house which talks about the Jack's Lantern. When you start searching about it more online, you see that no person was able to complete this game in their first attempt. You feel motivated and challenged by this Mystery House.  ")
time.sleep(2)
print(f"\nNext day morning, you call your friend \n{user_name.title()}- Hey Hector, where are you ?")
time.sleep(2)
print(f"Hector - Hey {user_name.title()}! I'm in my home. What's up man?")
print(f"{user_name.title()} - Alright look. I found this interesting Mystery Room idea and I want to solve the mystery to win. I heard that no one was able to complete this game man!! I feel excited. Would you join me?")
time.sleep(2)
print(f"Hector - Come on man, you are 23 years old and you say that you want to complete a game? Grow up dude!!")
time.sleep(2)
print(f"{user_name.title()}- Don't you wanna do something interesting? I'm bored with my life following the same old routine every day. Alright man, I am going to solve this with or without you. Its upto you now.")
print(f"Hector - You go ahead man. I got a lot going in my life and I don't have time to play games. Bye!!")
print(f"*cuts the call* ")

time.sleep(5)



##Game starts
def start():
  print("You arrive at the Beverly Hills where the Jack's Lanturn is located.\nA game master of Jack's Lantern approaches to you.\nDo you wanna talk to him? ")
  choice_1 = input("Type 'yes' to talk,\nType 'no' to ignore:\n")
  if choice_1 == 'yes':
    print(f"Hello, my name is {user_name.title()} and I am interested in this concept of escape room. Can you tell me the rules? .\nGame Master - This is called Jack's Lanturn. You should find the clues to solve the puzzle and by solving the puzzle you will get a key which unlocks the door to the next stage...\n It seems like you are only one member. Are you still willing to take the risk and finish this on your own?  ")
    print(f"{user_name.title()} - Sounds interesting. Sign me up. I will be the first to get out of the escape room.")
    time.sleep(3)
    print(f"Game Master - Don't say that I didn't warn you.Here are your keys to the main door. Good Luck!!  ")
    print("\nYou are given the keys to the main door.You need to find other keys to enter to other room.  ")
    print("\n   There are 5 rooms in this house- \nLiving \nGuest Bedroom \nLibrary \nDoll room \nMaster Bedroom")
    print("\n Remember, for every wrong move your game ends but you can restart again from the same stage. \n")

  elif choice_1 == 'no':
    print("I might as well talk to the game master who could give tips on how to solve the puzzles ")
    
    time.sleep(2)
    start()
  else:
    print("Please enter a valid option")
    start()
start()
time.sleep(5)
#Mission 1
print("\n")
print(f"Your adventure starts now.\nYou unlock the main door and enter, you get a spooky feeling and you are scared. ")
print(f"Your health is {health}% \nYou are given a backpack which can collect things you to need. \nYour inventory is empty. \nYou have {(len(coins))}. ")
time.sleep(2)

def adventure1():
  print("You enter living room. This room is a mess, in this mess you find a letter which says 'What has to be broken before you can use it?' ")
  print(f"{user_name.title()} - This  is a simple puzzle. The answer is EGG. Hold on, I need a key to get to next door and the answer to my puzzle is an egg. So the key should be inside the egg.")
  time.sleep(2)
  print("You find a diary. It could be useful for next stage. You pick the diary and keep it in your backpack")
  inventory.append("Diary")
  print("You search the whole surroundings again and now you find two eggs. One egg is heavy, other is light. What will you do now?")
  choice_2 = input("Which egg do you want to break? Heavy or Light\n")
  
  coins = []
  if choice_2 == 'heavy':
    print("You find the key to the Guest Bedroom. You also get 1 coin for solving this puzzle")
    coins.append(1)
    print(coins)
  elif choice_2 == 'light':
    print("Oops you broke the wrong egg. You game is over")
    print("Do you want start again?")
    death = input("Press '1' to start again or Press 'exit' to end the game: \n")
    if death == '1':
      adventure1()
    elif death == 'exit':
      sys.exit()
    else:
      print("Please enter a valid option")

    
    
  
  else :
    print("Please enter the valid option")
adventure1()

#Mission2
print("\n")
print("Welcome to Mission 2..")
print(f"Your health is {health}%")
print(f"Your inventory has {inventory}")
print(f"You have {(len(coins))} coins")
time.sleep(2)
print("\n")
def adventure2():
  print("You enter the Guest Bedroom. You find the puzzle on a dresser table. It says 'I have cities but no houses, I have mountains but no trees, I have water but no fish. What am I ?'")
  print(f"{user_name.title()} - What could this be? Every stage is getting tougher and tougher!!")
  print("You start searching the whole room to crack the puzzle. You search in your diary for any clues. You find a map of the house drawn inside the diary. Makes you think ")
  print(f"{user_name.title()} - This is the answer to the puzzle. But wait, why would the answer be a map? Maybe the next key is located somewhere in this map? ")
  print("You look at the map carefully and you notice that there are two keys in it. Maybe the other key could open the door in the next stage. You get the Library key which was hidden under the bed and you keep it in your backpack. But what about the other key?")
  time.sleep(2)
  choice_3 = input("Do you want to look for the other key?\n yes or no : ")
  if choice_3 == 'yes':
    print("You got tricked this time. This was a wrong move because the other key is duplicate.")
    print("Game over")
    print("Do you want to start the game again ?")
    death = input("Press '1' to start again or press 'exit' to end the game :\n")
    if death == '1':
      adventure2()
    elif death == 'exit' :
      sys.exit()
    else :
      print("Please enter a valid option")


    
    
  elif choice_3 == 'no':
    print("This other key might be a tricky one to distract me from completing the game fast. I will ignore this and move forward.")
    print("You do not loose any health but get 1 coin")
    coins.append(1)
  else :
    print("Please enter a valid option")
    adventure2()

adventure2()

#Mission 3
print("\n")
print("You move forward to the next stage. You open the Library room and enter inside")
print(f"Your health is {health}%. \nYour inventory has {inventory}. \nYou have {len(coins)} coins.") 
						
time.sleep(2)
def adventure3():
  print("This is a cruicial stage in the game. If you loose this round, you get eliminated directly. A wrong answer can eliminate the game and thus you have to play from the beginning again.")
  time.sleep(2)
  print("There are two puzzles you need to solve to get to the next stage. ") 
  print("You find a 'door knob'. You pick it and keep it in your bag")
  inventory.append('door knob') 
  print("You find a piece of paper which has the first puzzle. It says 'What disappears as soon as you say my name?'")
  print("Oh this time you get options to choose your answer. That should make it easy to answer.")
  choice_4 = input("Please choose from the below options - \nsilence \nnoise \n -")
  if choice_4 == 'silence':
    print("You get the right answer. Now you have to find the answer'silence' in the library")
    print("Maybe its a book name because we are inside the library")
    print("You find two books with the name 'Silence' in it. \nThe two books are \nSilence - Shusaku Endo \nSilence of the lambs -Thomas Harris")
    print("What will you choose?")
    choice_5 = input("silence \nsilence of the lambs :\n")
    if choice_5 == 'silence':
      print("You find the key. You get 1 coin for the correct answer. You move to the next stage")
      coins.append(1)
    elif choice_5 == 'silence of the lambs':
      print("That is the wrong answer. Your journey ends here. Better luck next time")
      death = input("Do you want to start over again? Press '1' to start again :\n ")
      if death == '1':
        adventure3()
      else:
        sys.exit()
    else :
      print("Please enter valid option")
  elif choice_4 == 'noise':
    print("You have chosen the wrong option. Your game ends here. Goodbye!!")
    death1 = input("Do you want to start over again? Press '1' to start again :\n")
    if death1 == '1':
      adventure3()
    else :

      sys.exit()
  else :
    print("Please enter valid option")
    adventure3()
adventure3()

#Mission 4
print("\n")
print(f"Your health is {health}% \nYour inventory contains {inventory} \nYour coin count is {len(coins)}")
time.sleep(2)


def adventure4():
  print("You enter the 4th stage of Jack's Lantern. The game gets tougher and tougher. So much at stake!!")
  print("You unlock the Doll Room. This room is very scary... Suddenly you hear strange soundss. I guess this is used to distract you from your game")
  print("..... But where is the puzzle? You can't find it any where")
  print("\n....")
  print(f"{user_name.title()} - How am I supposed to solve the puzzle if I can't find one... Let me search the dolls maybe I can find puzzle there")
  print("After 5 mins, you find a doll which has the puzzle. The puzzle says 'I come from a mine and get surrounded by the woods always.                      What am I?'")
  print(f"{user_name.title()} - What could this be? \nYou scratch your head on this.... ")
  print("You find a pencil shaped stuffed toy.. Do you want to check what is in it? What if it wrong? You get eliminated")
  choice_6 = input("Do you want to check what is inside the pencil shaped stuff toy?\nyes or no :")
  if choice_6 == 'yes':
    print("You find a key to the master bedroom. You get 1 coin ")
    coins.append(1)
    print("You move to the final stage of the game")
  elif choice_6 == 'no':
    print("You keep on looking for the right answer to the clue")
    print("Maybe it is present in the pencil.. ")
    adventure4()
  else :
    print("Please enter a valid option")
    adventure4()

adventure4()


time.sleep(5)
#Mission 5.. Final stage of the game
print("\n")
print(f"Your health is {health}% \nYour inventory has {inventory}\nYou have {len(coins)} coins")
print("This is the final stage of the game. This is where everything ends")
time.sleep(2)

def adventure5():
  print("Welcome to the final stage of Jack's Lantern")
  print("\n")
  print("You enter the Master bedroom and you notice a piece of paper... The paper says..")
  print("This is your final puzzle. If you answer this wrong, your game is over. You can restart the game from adventure 4. The final Riddle is")

  time.sleep(2)
  print("What word starts with E and ends with E but only has one letter in it? \nYour options are a.Eevee (a pokemon) \nb.Envelope \nc.Eye")
  choice_7 = input("Which option do you choose? \n a , b , c : \n")
  if choice_7 == 'a':
    print("Wrong answer.. Goodbye")
    death = input("Press '1' to start again.. Press 'exit' to quit. \n")
    if death == '1':
      adventure4()
    elif death == 'quit':
      sys.exit()
    else:
      print("Enter a valid option")
  elif choice_7 == 'b':
    print("You chose the right answer. Now search for your answer in the room")
    print("You win 1 coin")
    coins.append(1)
  elif choice_7 == 'c':
    print("Wrong answer.. Goodbye")
    death = input("Press '1' to start again.. Press 'exit' to quit. \n")
    if death == '1':
      adventure5()
    elif death == 'quit':
      sys.exit()
    else:
      print("Enter a valid option")
  else:
    print("Please enter a valid option")
adventure5()

## Game coming to an end... 
time.sleep(3)
print("You start searching for an envelope... After a few minutes, you find an envelope with a letter and a key..")
print("The letter says - Congratulations on completing the Jack's Lantern. ")
print(f"Your health is {health}% \nYour inventory has {inventory}. \nYou have total {len(coins)} coins")
print("\n")
print(f" Game Master - Thank you {user_name.title()} for playing my game. Hope to see you again!! ")
time.sleep(3)

#***************    THE GAME ENDS **********************#

#### Citations
#Concept - Escape Room
###  Wikimedia Foundation. (2021, October 31). Escape room. Wikipedia. Retrieved November 1, 2021, from https://en.wikipedia.org/wiki/Escape_room. 
#https://en.wikipedia.org/wiki/Escape_room



