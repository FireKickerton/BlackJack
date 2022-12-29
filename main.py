#Setup
#Allows random items from lists to be generated
import random

#Allows color, background, and brightness to be added to text
from colorama import Fore, Back, Style

#Allows pauses in the game so that everything isn't instantanious
import time

play = False

#The possible cards that can be drawn
Card_List = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
#Test List for Blackjack Win
#Card_List = ['J','A']

#Tracking record for wins and losses
playerWins = 0
dealerWins = 0
chips = 100



#Game
#The game repeats if the player has more than 0 chips and they want to play again via Ending Message
def playAgain():
  global playerWins
  global dealerWins
  global chips
  global bet
  playerBusted = False
  dealerBusted = False

  #Betting
  betPlaced = False
  while betPlaced == False:
    bet = input("Please input a bet >>> ")
    
    #If the input is an integer - prevents an error in the code
    if bet.isnumeric() == True:
      bet = int(bet)
      #If the bet is valid
      if bet <= chips and bet > 0:
        betPlaced = True
        time.sleep(1)
        print("----------------------------------------")
        
      #If the player does not have enough chips  
      elif bet > chips:
        print(Fore.RED + "You do not have enough chips!" + Style.RESET_ALL)

      elif bet <= 0:
        print(Fore.RED + "Bet too small!" + Style.RESET_ALL)
        
    #If the input is not valid 
    else:
      print(Fore.RED + "Invalid Response" + Style.RESET_ALL)


        
#First Card Draw for Player
  while play == True:
    Player_Ace_Count = 0
    Player_Ace_Used = 0
    #Generates a random Card
    Player_Card_1 = random.choice(Card_List)
    
    #If the Card is a Jack, Queen, or King
    if Player_Card_1 in ['J','Q','K']:
      print("Card 1 for Player: " + Player_Card_1)
      Player_Card_Value = 10
      Player_Total_Value = Player_Card_Value
      
    #If the Card is an Ace
    elif Player_Card_1 in ['A']:
      print("Card 1 for Player: " + Player_Card_1)
      Player_Card_Value = 11
      Player_Ace_Count = Player_Ace_Count + 1
      Player_Total_Value = Player_Card_Value
      
    #If the Card is a number
    else:
      print("Card 1 for Player: " + Player_Card_1)
      Player_Card_Value = Player_Card_1
      Player_Total_Value = int(Player_Card_Value)
      
    
    
#Second Card Draw for Player
    time.sleep(1)
    #Generates a random Card
    Player_Card_2 = random.choice(Card_List)
    
    #If the Card is a Jack, Queen, or King
    if Player_Card_2 in ['J','Q','K']:
      print("Card 2 for Player: " + Player_Card_2)
      Player_Card_Value = 10
      Player_Total_Value = Player_Total_Value + Player_Card_Value
      
    #If the Card is an Ace
    elif Player_Card_2 in ['A']:
      print("Card 2 for Player " + Player_Card_2)
      Player_Card_Value = 11
      Player_Ace_Count = Player_Ace_Count + 1
      Player_Total_Value = Player_Total_Value + Player_Card_Value
      
    #If the Card is a number
    else:
      print("Card 2 for Player: " + Player_Card_2)
      Player_Card_Value = Player_Card_2
      Player_Total_Value = Player_Total_Value + int(Player_Card_Value)

    #If the player's total value goes over 21 with an Ace in hand
    if Player_Ace_Count > Player_Ace_Used and Player_Total_Value > 21:
      Player_Total_Value = Player_Total_Value - 10
      Player_Ace_Used = Player_Ace_Used + 1
    
    #Prints the total value of the Player's Cards
    print("Total Value for Player: " + str(Player_Total_Value))
    print("----------------------------------------")
    
#BlackJack Check
    if int(Player_Total_Value) == 21:
      time.sleep(1)
      Dealer_Ace_Count = 0
      Dealer_Ace_Used = 0
      playerTurn = False
      dealerTurn = False
      #Generates a random Card
      Dealer_Card = random.choice(Card_List)
      
      #If the Card is a Jack, Queen, or King
      if Dealer_Card in ['J','Q','K']:
        print("Card 1 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = 10
        Dealer_Total_Value = Dealer_Card_Value
        
      #If the Card is an Ace
      elif Dealer_Card in ['A']:
        print("Card 1 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = 11
        Dealer_Ace_Count = Dealer_Ace_Count + 1
        Dealer_Total_Value =  Dealer_Card_Value
        
      #If the Card is a number
      else:
        print("Card 1 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = Dealer_Card
        Dealer_Total_Value = int(Dealer_Card_Value)


      
      time.sleep(1)
      #Generates a random Card
      Dealer_Card = random.choice(Card_List)
      
      #If the Card is a Jack, Queen, or King
      if Dealer_Card in ['J','Q','K']:
        print("Card 2 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = 10
        Dealer_Total_Value = Dealer_Total_Value + Dealer_Card_Value
        
      #If the Card is an Ace
      elif Dealer_Card in ['A']:
        print("Card 2 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = 11   
        Dealer_Ace_Count = Dealer_Ace_Count + 1
        Dealer_Total_Value = Dealer_Total_Value + Dealer_Card_Value
        
      #If the Card is a number
      else:
        print("Card 2 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = Dealer_Card
        Dealer_Total_Value = Dealer_Total_Value + int(Dealer_Card_Value)
        
      #If the player's total value goes over 21 with an Ace in hand
      if Dealer_Ace_Count > Dealer_Ace_Used and Dealer_Total_Value > 21:
        Dealer_Total_Value = Dealer_Total_Value - 10
        Dealer_Ace_Used = Dealer_Ace_Used + 1
      print("Total Value for Dealer: " + str(Dealer_Total_Value))
        
      #If the Dealer also gets a Blackjack
      if Dealer_Total_Value == 21:
        result = 'draw'
        print("----------------------------------------")
        time.sleep(1)
        gameEnd(result, playerBusted, dealerBusted)
        
      #If the Dealer did not get a BlackJack
      elif Dealer_Total_Value < Player_Total_Value or Dealer_Total_Value > 21:
        result = 'blackjack'
        print("----------------------------------------")
        time.sleep(1)
      gameEnd(result, playerBusted, dealerBusted)
      

      
#First Card Draw for Dealer
    if play != True:
      break
    else:
      time.sleep(1)
      Dealer_Ace_Count = 0
      Dealer_Ace_Used = 0
      
      #Generates a random Card
      Dealer_Card = random.choice(Card_List)
      
      #If the Card is a Jack, Queen, or King
      if Dealer_Card in ['J','Q','K']:
        print("Card 1 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = 10
        Dealer_Total_Value = Dealer_Card_Value
        
      #If the Card is an Ace
      elif Dealer_Card in ['A']:
        print("Card 1 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = 11      
        Dealer_Ace_Count = Dealer_Ace_Count + 1
        Dealer_Total_Value = Dealer_Card_Value
        
      #If the Card is a number  
      else:
        print("Card 1 for Dealer: " + Dealer_Card)
        Dealer_Card_Value = Dealer_Card
        Dealer_Total_Value = int(Dealer_Card_Value)
        
      #Prints the total value of the Dealer's Cards
      print("Total Value for Dealer: " + str(Dealer_Total_Value))
        
      break
  
  
    
#Multiple Card Draws for Player
  time.sleep(1)
  Card_Number = 3
  playerTurn = True
  while playerTurn == True and play == True:
    print("----------------------------------------")
    
    #Console asking for an input
    answer = input("Do you want to hit(h) or stand(s)? >>> ")
#Hit
    if answer in ['h','H','hit','Hit']:
      time.sleep(1)
      
      #Generates a random Card
      Player_Card = random.choice(Card_List)
                                 
      #If the Card is a Jack, Queen, or King
      if Player_Card in ['J','Q','K']:
        print("Card " + str(Card_Number) + " for Player: " + Player_Card)
        Player_Card_Value = 10
        Player_Total_Value = Player_Total_Value + Player_Card_Value
      
        #If the Card is an Ace
      elif Player_Card in ['A']:
        print("Card " + str(Card_Number) + " for Player: " + Player_Card)
        Player_Card_Value = 11
        Player_Ace_Count = Player_Ace_Count + 1
        Player_Total_Value = Player_Total_Value + Player_Card_Value
        
      #If the Card is a number
      else:
        print("Card " + str(Card_Number) + " for Player: " + Player_Card)
        Player_Card_Value = Player_Card
        Player_Total_Value = Player_Total_Value + int(Player_Card_Value)

      #If the Player's total value goes over 21 with an Ace in hand
      if Player_Ace_Count > Player_Ace_Used and Player_Total_Value > 21:
        Player_Total_Value = Player_Total_Value - 10
        Player_Ace_Used = Player_Ace_Used + 1
      print("Total Value for Player: " + str(Player_Total_Value))
      playerTurn = False
      Card_Number = Card_Number + 1
      
#Stand
    elif answer in ['s','S','stand','Stand']:
      playerBusted = False
      playerTurn = False
      dealerTurn = True
      print("----------------------------------------")
      break
      
#Invalid Answers
    elif answer not in ['h','H','hit','Hit','s','S','stand','Stand']:
      print("----------------------------------------")
      print(Fore.RED + "Invalid Response." + Style.RESET_ALL)
      
#Checking if Player has Busted
    if Player_Total_Value < 22:
      playerTurn = True
      
    elif Player_Total_Value > 21:
      playerBusted = True
      dealerBusted = False
      dealerTurn = False
      result = 'lose'
      print("----------------------------------------")
      time.sleep(1)
      gameEnd(result, playerBusted, dealerBusted)
  
  
  
#Multiple Draws for Dealer  
  Card_Number = 2
  
  while dealerTurn == True:
    #Generates a random Card
    Dealer_Card = random.choice(Card_List)
    
    #If the Card is a Jack, Queen, or King
    if Dealer_Card in ['J','Q','K']:
      print("Card " + str(Card_Number) + " for Dealer: " + Dealer_Card)
      Dealer_Card_Value = 10
      Dealer_Total_Value = Dealer_Total_Value + int(Dealer_Card_Value)
      
      #If the Card is an Ace
    elif Dealer_Card in ['A']:
      print("Card " + str(Card_Number) + " for Dealer: " + Dealer_Card)
      Dealer_Card_Value = 11
      Dealer_Ace_Count = Dealer_Ace_Count + 1
      Dealer_Total_Value = Dealer_Total_Value + Dealer_Card_Value
      
    #If the Card is a number
    else:
      print("Card " + str(Card_Number) + " for Dealer: " + Dealer_Card)
      Dealer_Card_Value = Dealer_Card
      Dealer_Total_Value = Dealer_Total_Value + int(Dealer_Card_Value)
      
    #If the Dealer's total value goes over 21 with an Ace in hand  
    if Dealer_Ace_Count > Dealer_Ace_Used and Dealer_Total_Value > 21:
      Dealer_Total_Value = Dealer_Total_Value - 10
      Dealer_Ace_Used = Dealer_Ace_Used + 1
    print("Total Value for Dealer: " + str(Dealer_Total_Value))
    print("----------------------------------------")
    Card_Number = Card_Number + 1
    time.sleep(1)
  
#Checking if Dealer can Draw Cards
    if Dealer_Total_Value < 22:
      dealerBusted = False
      
    if Dealer_Total_Value > 21:
      dealerBusted = True
      result = 'win'
      gameEnd(result, playerBusted, dealerBusted)
      break
      
    elif Dealer_Total_Value > 16:
      dealerTurn = False


      
#Checking Result
    if dealerTurn == False and dealerBusted == False:
      if Player_Total_Value > Dealer_Total_Value:
        result = 'win'
        
      elif Player_Total_Value == Dealer_Total_Value:
        result = 'draw'
        
      elif Player_Total_Value < Dealer_Total_Value:
        result = 'lose'
        
      gameEnd(result, playerBusted, dealerBusted)


      
#Ending Message
def gameEnd(result, playerBusted, dealerBusted):
  global playerWins
  global dealerWins
  global chips
  global bet
  
#Result
  #If the Player won
  if result == 'win':
    playerWins = playerWins + 1
    print(Fore.GREEN)
    
    #If the Player won because the dealer went over 21
    if dealerBusted == True:
      print("You win!  The dealer went over 21!")
      
    #If the Player won when the dealer did not go over 21
    elif dealerBusted == False:
      print("You win!  You had a greater value of cards than the dealer!")
      
  #If the Player had the same total value as the Dealer
  elif result == 'draw':
    print(Fore.YELLOW + Style.BRIGHT)
    print("It's a draw!  You had an equal value of cards compared to the dealer!")
    
  #If the Player lost
  elif result == 'lose':
    dealerWins = dealerWins + 1
    print(Fore.RED)
    
    #If the Player went over 21
    if playerBusted == True:
      print("You lose!  You went over 21!")
      
    #If the Player had a total value less than the Dealer's total value
    elif playerBusted == False:
      print("You lose!  The dealer had a greater value of cards than you!")

  elif result == 'blackjack':
    playerWins = playerWins + 1
    print(Fore.GREEN + Style.BRIGHT)
    print("BlackJack!!!")
  print("")
  
#ASCII Art
  print("          `-:+oooo+:.            `-:///:-`")        
  print("        .+syyyyyyyyyys/`      ./oyyyyyyyyyo/`")     
  print("      .+ssssssssssssss/`    .+ssssssssssssss+`")    
  print("     :ssssssso+//+os+.     :ssssssssooosss+.")      
  print("    :oooooo:`      .      /oooooo/-`   `--")        
  print("   .ooooo+`         ``.` :ooooo/`            ``")   
  print("   /oooo+`    -+++ooooo``ooooo/     -:://++ooo+")   
  print("   ooooo/     /+/+ooooo -ooooo.    `osoooooooo/")   
  print("   osssso`       -sssso -sssss-     `  /ssssss.")   
  print("   :ssssso-`  `-+ssssss``ssssss-     ./ssssss-")    
  print("    +ssssssyssyssssss+.  -sssssss+++ssssssso.")     
  print("     -syyyyyyyyyyys/.     -syyyyyyyyyyyyy+-")       
  print("       .:+oooo+/-`          -+syyyyyso/-`")   
  print(Style.RESET_ALL)
  print(Fore.GREEN + str(playerWins) + Style.RESET_ALL + " - " + Fore.RED + str(dealerWins) + Style.RESET_ALL)
  print("")
  playAgainInput = False

  #If the Player won
  if result == 'win':
    chips = chips + bet
    
  #If the player lost
  elif result == 'lose':
    chips = chips - bet
    
  #If the player won with a blackjack
  elif result == 'blackjack':
    chips = chips + (bet * 1.5)
    #if bet % 2 != 0:
      #chips = chips + 0.5
    round(chips)

  
  print("You have " + Fore.YELLOW + str(chips) + Style.RESET_ALL + " chips.")
  
#Checking if the player has 0 chips
  if chips == 0:
    playAgainInput = True
    noChipsLeft()
  print("")
  time.sleep(1)
  

  

  
#Play Again Messages
  while playAgainInput == False:
    answer = input("Do you want to play again? (y/n) >>> ")
    
    #If the Player wants to play again
    if answer == 'y':
      playAgainInput = True
      print("")
      print("----------------------------------------")
      playAgain()
      
    #If the Player does not want to play again
    elif answer == 'n':
      playAgainInput = True
      print("")
      print(Fore.GREEN + "Thanks for playing!  Hope you had fun!" + Style.RESET_ALL)
      
    #Invalid Response
    elif answer != 'y' or 'n':
      print(Fore.RED + "Invalid Response" + Style.RESET_ALL)


      
#No Chips Left
def noChipsLeft():
  global play
  print("")
  print(Fore.RED + "Oh no!  You ran out of chips.  Sorry :(" + Style.RESET_ALL)   
  print("")
  print(Fore.GREEN + Style.BRIGHT + "Thanks for playing BlackJack!!!" + Style.RESET_ALL)
  play = False



  
#Starting Message
print("Welcome to BlackJack!")
time.sleep(1)
while play == False and chips != 0:
  answer = input("Do you want to play(p) or see the rules(r) first? >>> ")


  
#Play
  if answer in ['p', 'P', 'play', 'Play']:
    play = True
    time.sleep(1)
    print("")
    print("----------------------------------------")
    print("You have " + Fore.YELLOW + Style.BRIGHT + "100 " + Style.RESET_ALL + "chips to start out with.")
    playAgain()

#Rules
  elif answer in ['r', 'R', 'rules', 'Rules']:
    print("")
    print("BlackJack is a card game that is played between a player and a dealer.")
    time.sleep(3)
    print("The goal is to have your card value be as close to 21 as possible without going over.")
    time.sleep(4.5)
    print("You are given two cards in the beginning.")
    time.sleep(2.5)
    print("Each card has a value of the number that is on it.")
    time.sleep(2.5)
    print("If a card has a Jack(J), Queen(Q), or King(K) on it, that card has a value of 10.")
    time.sleep(4)
    print("However, if the card has an Ace(A) on it, that card has a value of 11.")
    time.sleep(3.5)
    print("If your card value goes over 21 while you have an Ace(A), the value of the card will change to 1.")
    time.sleep(4.5)
    print("Every turn, you can choose to hit(gain a card), or stand(stop gaining cards).")
    time.sleep(4)
    print("If your card value goes over 21, you lose the game.")
    time.sleep(3)
    print("Once you stand, the dealer will draw cards until their card value hits 17 or higher.")
    time.sleep(4)
    print("In the end, whoever has the greater card value wins the game!")
    time.sleep(3)
    print("")
    
  #Invalid Response
  elif answer not in ['p', 'P', 'play', 'Play', 'r', 'R', 'rules', 'Rules']:
    print(Fore.RED + "Invalid Response" + Style.RESET_ALL)