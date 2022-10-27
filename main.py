#Unlimited deck size. You can draw any card. No joker. 
#If you draw ace and it exceeds 21, its value turns into 1.
#The cards in the list have equal probability of being drawn.
#Cards are not removed from the deck as they are drawn.

from replit import clear
from art import logo
from random import choice

#is_playing for repeating game
is_playing = True
while is_playing:
  ask_if_play = input(
    'Do you want to play a game of Blackjack? Type "y" for yes, "n" for no:\n'
  ).lower()
  if ask_if_play == "y":
    clear()
    print(logo + "\n")
  elif ask_if_play == "n":
    clear()
    print(logo + "\n")
    print("Of course you do. What did you come here for?\n")
  else:
    clear()
    print(logo + "\n")
    print("You mistyped but I assume you want to play game of blackjack.\n")

  #11 is ace, up to 10 normal numbers, and last three 10's acts as Jack, Queen, King value
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = []
  ai_cards = []
  player_total_score = 0
  ai_total_score = 0
  
  #used when game ends, prints final results
  def final_text():
    print(f"Your final hand: {player_cards}, final score: {player_total_score}\nComputer's final hand: {ai_cards}, final score: {ai_total_score}\n")
    
  #If player decides to not draw more cards, 
  #computer starts to draw cards until it reaches more than 16 total value.
  #Also, this is final stage function, where total score is compared to computer score.
  def torp_question_choice():
  
    global ai_total_score
  
    while ai_total_score < 17:
      add_ai_card()
      ai_total_score = sum(ai_cards)
    if ai_total_score > 21:
      final_text()
      print("You win.\n")
      return
    if ai_total_score == 21 and player_total_score == 21:
      final_text()
      print("You lose against blackjack.\n")
      return
    elif ai_total_score > player_total_score:
      final_text()
      print("You lose.\n")
      return
    elif ai_total_score == player_total_score:
      final_text()
      print("It's a draw.\n")
      return
    elif ai_total_score < player_total_score:
      final_text()
      print("You win.\n")
      return
      
  #add random card to player or computer
  def add_player_card():
    player_cards.append(choice(deck))
  def add_ai_card():
    ai_cards.append(choice(deck))
    
  #calling functions to draw two cards for player and computer to start game
  add_player_card()
  add_player_card()
  add_ai_card()
  add_ai_card()
  
  #recursion here, when player decides to draw another card, code repeats
  def player_drawn_card():
  
    global player_total_score
    global ai_total_score
    
  #total score from player and computer hands
    player_total_score = sum(player_cards)
    ai_total_score = sum(ai_cards)

    #if and else to check if player or computer immidiately draws blackjack from the start of the game.
    #if computer and player draw 21, computer wins
    if player_total_score == 21 and ai_total_score < 21:
      print(f"Your final hand: {player_cards}, final score: {player_total_score}\nComputer's final hand: {ai_cards}, final score: {ai_total_score}\n")
      print("You won with blackjack.\n")
      return
    elif ai_total_score == 21 and player_total_score <= 21:
      print(f"Your final hand: {player_cards}, final score: {player_total_score}\nComputer's final hand: {ai_cards}, final score: {ai_total_score}\n")
      print("You lost against blackjack.\n")
      return

    #prints current state of game
    if player_total_score < 21 and ai_total_score < 21:
      print(f'Your cards {player_cards}, current score {player_total_score}.\nComputer first card: {ai_cards[0]}\n')

    #Loop to check if player has ace and exceeds 21. If yes, it turns into 1. 
    #Then if value is 21, players wins. If less than 21, it prints current state.
    #If turned into 1 and still exceeds 21, player loses.
    if player_total_score > 21:
      if 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
        player_total_score = sum(player_cards)
        if player_total_score == 21:
          print(f"Your final hand: {player_cards}, final score: {player_total_score}\nComputer's final hand: {ai_cards}, final score: {ai_total_score}\n")
          print("You won with blackjack.\n")
          return
        elif player_total_score < 21:
          print(f'Your cards {player_cards}, current score {player_total_score}.\nComputer first card: {ai_cards[0]}\n')
        if player_total_score > 21:
          final_text()
          print("You lose.\n")
          return
      else:
        final_text()
        print("You lose.\n")
        return

    #Loop for asking player if he wants to draw another card, if yes, recursion starts
    #If no, goes to torp_question_choice(), to final stage of game
    take_or_pass = True
    while take_or_pass:
      torp_question = input(
        'Type "y" to get another card or "n" to pass:\n').lower()
      if torp_question == "y":
        add_player_card()
        take_or_pass = False
        player_drawn_card()
      elif torp_question == "n":
        take_or_pass = False
        torp_question_choice()
      else:
        print('Wrong input. Try again.\n')
      
  #to start recursion
  player_drawn_card()
    
    
    
  


