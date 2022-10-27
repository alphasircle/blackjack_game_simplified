from replit import clear
from art import logo
from random import choice

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
    

  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = []
  ai_cards = []
  player_total_score = 0
  ai_total_score = 0
  
  
  def final_text():
    print(f"Your final hand: {player_cards}, final score: {player_total_score}\nComputer's final hand: {ai_cards}, final score: {ai_total_score}\n")
  
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
  
  def add_player_card():
    player_cards.append(choice(deck))
  def add_ai_card():
    ai_cards.append(choice(deck))
  
  add_player_card()
  add_player_card()
  add_ai_card()
  add_ai_card()
  
  def player_drawn_card():
  
    global player_total_score
    global ai_total_score
  
    player_total_score = sum(player_cards)
    ai_total_score = sum(ai_cards)
    
    if player_total_score == 21 and ai_total_score < 21:
      print(f"Your final hand: {player_cards}, final score: {player_total_score}\nComputer's final hand: {ai_cards}, final score: {ai_total_score}\n")
      print("You won with blackjack.\n")
      return
    elif ai_total_score == 21 and player_total_score <= 21:
      print(f"Your final hand: {player_cards}, final score: {player_total_score}\nComputer's final hand: {ai_cards}, final score: {ai_total_score}\n")
      print("You lost against blackjack.\n")
      return
  
    if player_total_score < 21 and ai_total_score < 21:
      print(f'Your cards {player_cards}, current score {player_total_score}.\nComputer first card: {ai_cards[0]}\n')
    
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
      
  
  player_drawn_card()
    
    
    
  


