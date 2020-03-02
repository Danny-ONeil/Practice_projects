import random

money = 100

#Write your game of chance functions here



#----------------------------------------------------------------------------------------------------------------------------Below is the code for betting on flipping a coin-------------------------------------------------------------------------------------------------------------------------------
def flip_coin(bet,guess):
  #making sure they eneter in the correct form of Heads or Tails
  if guess != 'Heads' and guess != 'Tails':
    print("------------------")
    print('You didnt enter your guess in the correct format, Make sure to enter your guess as Heads or Tails')
    print("------------------")
    return 0
  
  #making sure the you bet is more than 0
  if bet <= 0:
    print("------------------")
    print('Your bet needs to be larger than 0')
    print("------------------")
    return 0
  
  
  #starting the game of flipping a coin
  print("------------------")
  print('Lets Flip a Coin')
  print('You bet $'+ str(bet)+', It will land on '+ str(guess))
  result = random.randint(1,2)
  
  #Figuring out what the coin landed on
  if result == 1:
    print('The coin landed on Heads!!')
  else:
    print('The coin landed on Tails!!')
    
  #Determining if you chose what side of the coin it landed on correctly and how much money you won or lost
  if (guess == 'Heads' and result == 1) or (guess == 'Tails' and result == 2):
    print('You won $' + str(bet))
    print("------------------")
    return bet
  else:
    print('You lost $'+str(bet))
    print("------------------")
    return -bet
 
#print(flip_coin(10,'Heads'))


#----------------------------------------------------------------------------------------------------------------------------Below is the code for betting on a game of Cho Han-----------------------------------------------------------------------------------------------------------------------------
def cho_han(bet,guess):
  #making sure they enter in the correct form of odd or Even
  if guess != 'Even' and guess != 'Odd':
    print("------------------")
    print('You didnt enter your guess in the correct format, Make sure to enter your guess as odd or Even')
    print("------------------")
    return 0
  
    #making sure the your bet is more than 0
  if bet <= 0:
    print("------------------")
    print('Your bet needs to be larger than 0')
    print("------------------")
    return 0
  
  
  print("------------------")
  print('Lets play Cho Han')
  print('You bet $'+ str(bet)+ ', the sum of the dice will be '+ str(guess))
  die_1 = random.randint(1,6)
  die_2 = random.randint(1,6)
  result = (die_1 + die_2) % 2
  #Printing out what the sum of the 2 dice are
  if result == 0:
    print('The sum of the dice is Even!!')
  else:
    print('The sum of the dice is Odd!!')
  #Determining if you choose odd or even right to the sum and how much you either won or lost 
  if (guess == 'Even' and result == 0) or (guess == 'Odd' and result == 1):
    print('You won  $'+ str(bet))
    print("------------------")
    return bet
  else:
    print('You lost $'+ str(bet))
    print("------------------")
    return -bet
  
#print(cho_han(20,'Odd'))


#----------------------------------------------------------------------------------------------------------------------------Below is the code for betting on picking a higher card than another player from a deck of 1-10 --------------------------------------------------------------------------------------------------------------------------------------------
def pick_card(bet):
    #making sure the your bet is more than 0
  if bet <= 0:
    print("------------------")
    print('Your bet needs to be larger than 0')
    print("------------------")
    return 0 
  
  
  print("------------------")
  print("Lets play who can pick a higher card, from a deck 1-10")
  print('You bet $' + str(bet)+ ', you will pick a higher card than player 2')
  player_1 = random.randint(1,10)
  player_2 = random.randint(1,10)
  print('You picked a ' + str(player_1))
  print('Player 2 picked a '+ str(player_2))
  #Determining what player picked out a higher card and then determining how much money you won or you lost
  if player_1 > player_2:
    print('You won $'+ str(bet))
    print("------------------")
    return bet
  elif player_1 < player_2:
    print('You lost $' + str(bet))
    print("------------------")
    return -bet
  else:
    print('You tied, you get your money back')
    print("------------------")
    return 0

#print(pick_card(20))



#----------------------------------------------------------------------------------------------------------------------------Below is the code for betting on the game of Roulette, just only picking odd or even-------------------------------------------------------------------------------------------------------------------------------------------------------
def roulette(bet,guess):
  #making sure they enter in the correct form of odd or Even
  if guess != 'Even' and guess != 'Odd':
    print("------------------")
    print('You didnt enter your guess in the correct format, Make sure to enter your guess as odd or Even')
    print("------------------")
    return 0
  
    #making sure the your bet is more than 0
  if bet <= 0:
    print("------------------")
    print('Your bet needs to be larger than 0')
    print("------------------")
    return 0  
  
  print("------------------")
  print('Lets play some roulette')
  print('You bet $'+ str(bet)+ ', it will land on an '+ str(guess))
  result = random.randint(1,38)
  #Printing out what the ball landed on 
  if result == 37:
    print('The ball landed on 0')
  elif result == 38:
    print('The ball landed on 00')
  else:
    print('The ball landed on ' + str(result))
  
  #Determing if you guessed correctly if the ball landed on even or odd, note landing on either 0, 00 results in guessing incorect
  if (guess == 'Even' and result % 2 == 0 and (result != 37 or result != 38)) or (guess == 'Odd' and result % 2 == 1 and (result != 37 or result != 38)):
    print('You won $' + str(bet))
    print("------------------")
    return bet
  else:
    print('You lost $' + str(bet))
    print("------------------")
    return -bet

#print(roulette(12,'Odd'))


#roulette(bet,guess)
#flip_coin(bet,guess)
#cho_han(bet,guess)
#pick_card(bet)

money += flip_coin(10,"Heads")
money += flip_coin(15,'Tails')
money += cho_han(30,'Odd')
money += pick_card(50)
money += roulette(40,'Even')

print('I finshed with $' + str(money))







#Call your game of chance functions here
