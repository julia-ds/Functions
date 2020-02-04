#The project has a variable named money that starts at 100. This represents your current amount of money. In every game of chance, you will be able to bet money. The value of money should change depending on whether you win or lose the game. Your functions should have print statements to help the user understand what has happened. For example, in games of chance that involve rolling dice, you should print out the result of those dice rolls. You should also print whether the player won or lost the game, and how much money they won or lost.
import random
money = 100

#Create a function that simulates flipping a coin and calling either "Heads" or "Tails". This function (along with all of the other functions you will write in this project) should have a parameter that represents how much the player is betting on the coin flip.
def flip_coin(bet, guess):
  if money == 0 or bet > money:
    return print('Sorry, you do not have enough money!')
  result = random.randint(1, 2)
  if result == 1:
    print("Heads!")
  elif result == 2:
    print("Tails!")
  if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
    print("Congratulations! You won " + str(bet)+ " dollars!")
    return bet
  else: 
    print("Sorry, you lost " + str(bet)+ " dollars!")
    return -bet
  
# Create a function that simulates playing the game Cho-Han. The function should simulate rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.
def cho_han(bet, guess):
  if money == 0 or bet > money:
    return print('Sorry, you do not have enough money!')
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  result = dice1 + dice2
  if result % 2 == 0:
    print('Even!')
  elif result % 2 != 0:
    print('Odd')
  if (guess == 'Even' and result % 2 == 0) or (guess == 'Odd' and result % 2 != 0):
    print('Congratulations! You won ' + str(bet)+ ' dollars!')
    return bet
  else: 
    print('Sorry, you lost ' + str(bet)+ ' dollars!')
    return -bet

# Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins. There are no jokers in the deck.
def pick_card(bet):
  if money == 0 or bet > money:
    return print('Sorry, you do not have enough money!')
  player_1 = random.randint(2, 13)
  player_2 = random.randint(2, 13)
  if player_1 > player_2:
    print('Your card is ' + str(player_1) + ' which is bigger than your opponent\'s ' + str(player_2) + '. Congratulations! You won ' + str(bet)+ ' dollars!')
    return bet
  elif player_1 < player_2:
    print('Your card is ' + str(player_1) + ' which is smaller than your opponent\'s ' + str(player_2) + '. Sorry, You lost ' + str(bet)+ ' dollars!')
    return -bet
  else:
    print('It\'s a tie! Please try again')
    return 0

#Create a function that simulates some of the rules of roulette. A random number should be generated that determines which space the ball lands on.
def roulette(bet, guess):
  if money == 0 or bet > money:
    return print('Sorry, you do not have enough money!')
  result = random.randint(0, 36)
  print('The wheel has landed on ' + str(result))
  # Here we bet on the wheel stopping at an even number or an odd one
  if (guess == 'odd' and result % 2 != 0) or (guess == 'even' and result % 2 == 0):
    print('Your guess ' + str(guess) + ' was riht! Congratulations! You won ' + str(bet) + ' dollars!')
    return bet
  # Here we bet on the wheel stopping at a red number or a black one
  elif (guess == 'red' and result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]) or (guess == 'black' and result in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]):
    print('Your guess ' + str(guess) + ' was riht! Congratulations! You won ' + str(bet) + ' dollars!')
    return bet
  # Here we bet whether the wheel stops at a big number or a small one
  elif (guess == '1 to 18' and result in range(1, 19)) or (guess == '19 to 36' and result in range(19, 37)):
    print('Your guess ' + str(guess) + ' was riht! Congratulations! You won ' + str(bet) + ' dollars!')
    return bet
  # Here we just trying to guess a number at which the wheel should stop
  elif guess == result:
    print('Your guess ' + str(guess) + ' was riht! Congratulations! You won ' + str(bet) + ' dollars!')
    return bet
  # If nothing mentioned above was true, then we lost
  else:
    print('Your guess was ' + str(guess) + ' . Sorry, you lost ' + str(bet) + ' dollars!')
    return -bet

# Here I check my functions taking into account the money one has for the bets
money += flip_coin(10, 'Heads')
money += cho_han(5, 'Odd')
money += pick_card(5)
money += roulette(10, 'black')

