# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:51:36 2020

@author: 220316
"""

import random
import numpy as np
import time

class Eruption:
    
    registry = []
    
    def __init__(self,name,country,year,vei,num_deaths):
        self.registry.append(self) # Creating a registry to allow me to iterate through objects created in class
        self.name = name # name of volcano
        self.country = country # country that volcano is in
        self.year = year # year of eruption (most recent wins)
        self.vei = vei # VEI of eruption (largest wins)
        self.num_deaths = num_deaths # Number of deaths (most wins)     

    def display_card(self):
        print(
            '\nVolcano: '+self.name+', '+self.country
            +'\n1. Year of eruption: '+str(self.year)
            +'\n2. Volcanic Explosivity Index: '+str(self.vei)
            +'\n3. Estimated number of casualties: '+str(self.num_deaths)
            )
        
class Player:
    def __init__(self,num,name):
        self.num = num # player number
        self.name = name # player name
        self.cards = []
    
    def greet(self):
        print(f"{self.name} has been added to the game")

def slow_print(text):
    time.sleep(2)
    print(text)
    
def introduction():
    print("""
          Let's play Volcano Top Trumps!
          
          In this edition, each card represents a single historic volcanic eruption.
          
          The first player must select one of the following categories:
              
              1. Year of eruption (most recent eruption wins)
              2. Volcanic explosivity index (highest value wins)
              3. Estimated number of casualties (most casualties wins)
          
          The winner of each round takes the cards of the other players, and placed at the bottom
          of their pile. In the event of a tie, the round is replayed with the same cards. 
          A new category must be chosen.
          
          If you have no cards left, you are knocked out of the game.
          
          The winner is the player who has all the cards at the end of the game.
          
          Okay, let's play!
          
          """)

def shuffle_deck(deck):
    return random.shuffle(deck)

def split_deck(deck,players):
    num_players = len(players)
    for idx, player in enumerate(players):
        player.cards = list(np.array_split(deck,num_players)[idx])

def select_who_goes_first(players):
    slow_print('\nRandomly selecting who goes first...')
    random.shuffle(players)
    player1 = players[0]
    slow_print(f'{player1.name} will go first')
    return players

def play_round(players):
    slow_print(f"\nOkay {players[0].name}, it's your turn."
          +" Here's your next card:")
    players[0].cards[0].display_card()
    num = 0
    while num not in [1,2,3]:
        ans = input("Select a category by entering the category number: ")
        try:
            num = int(ans)
        except:
            continue
    if num == 1:
        slow_print(f"\n{players[0].name} selected the {players[0].cards[0].year} eruption of {players[0].cards[0].name} ")
        values = []
        for player in players:
            values.append(player.cards[0].year)
        for player in players[1:]:
            slow_print(f"Card of {player.name}: The eruption of {player.cards[0].name} in {player.cards[0].year}")
        winner = values.index(max(values)) # Winner is the most recent year
        
    elif num == 2:
        slow_print(f"The {players[0].cards[0].year} eruption of {players[0].cards[0].name} had a VEI of {players[0].cards[0].vei}")
        values = []
        for player in players:
            values.append(player.cards[0].vei)
        for player in players[1:]:
            slow_print(f"Card of {player.name}: The {player.cards[0].year} eruption of {player.cards[0].name} had a VEI of {player.cards[0].vei}")
        winner = values.index(max(values)) # Winner is the eruption wtih the highest VEI
        
    elif num == 3:
        slow_print(f"The {players[0].cards[0].year} eruption of {players[0].cards[0].name} lead to the deaths of an estimated {players[0].cards[0].num_deaths} people")
        values = []
        for player in players:
            values.append(player.cards[0].num_deaths)
        for player in players[1:]:
            slow_print(f"Card of {player.name}: The {player.cards[0].year} eruption of {player.cards[0].name} led to the deaths of an estimated {player.cards[0].num_deaths} people")
        winner = values.index(max(values)) # Winner is the eruption with the most casualties
    
    if values.count(max(values)) > 1:
        slow_print('Its a tie! Play the round again!')
    else:
        slow_print(f"\n{players[winner].name} wins the round and collects the cards")
        round_cards = []
        for player in players:
            round_cards.append(player.cards[0]) # Adding the cards from that round to a list
            del player.cards[0] # Remove first card from the players hand
        
        for round_card in round_cards:
            players[winner].cards.append(round_card)
        
        for player in players:
            num_cards = len(player.cards)
            slow_print(f'{player.name} has {num_cards} cards left')
            if num_cards == 0:
                slow_print(f'{player.name} has been knocked out of the game!')
                
        
        players[winner],players[0] = players[0],players[winner] # Moving winner to beginning of list, their go next
        
    
         
def main():
    
    introduction()
    
    eruptions = [
    Eruption('Mount Pinatubo','Philippines',1991,6,847),
    Eruption('Krakatoa','Indonesia',1883,6,36000),
    Eruption('Eyjafjallajökull','Iceland',2010,4,0),
    Eruption('Mount Tambora','Indonesia',1815,7,71000),
    Eruption('Nevado del Ruiz', 'Colombia', 1985,3,23000),
    Eruption('Mount Vesuvius', 'Italy',79,5,13000),
    Eruption('Novarupta','USA',1912,6,0),
    Eruption('Mount Agung','Indonesia',1963,5,1584),
    Eruption('La Soufrière','St. Vincent',1902,5,1680),
    Eruption('Mount Unzen','Japan',1792,2,15000),
    Eruption('Mount Pelée','Martinique',1902,4,30000),
    Eruption('Whakaari','New Zealand',2019,2,21),
    Eruption('Mount Nyiragongo','Democratic Republic of the Congo',2002,1,245),
    Eruption('Mount St. Helens','USA',1980,5,57),
    Eruption('Arenal Volcano','Costa Rica',1968,3,87),
    Eruption('Kilauea','USA',1790,4,400),
    Eruption('Mount Ontake','Japan',2014,3,63),
    Eruption('Kelud','Indonesia',1586,5,10000),
    Eruption('Mount Lamington','Papua New Guinea',1951,4,2942),
    Eruption('Mount Galunggung','Indonesia',1822,5,4011),
    Eruption('Mount Asama','Japan',1783,4,1151),
    Eruption('El Chichón','Mexico',1982,5,1900),
    Eruption('Santa María','Guatemala',1902,6,6000),
    Eruption('Mount Hudson','Chile',1991,5,0)
    ]
    
    num_players = 0
    while num_players not in [2,3,4]:
        ans = input("How many people are playing? (2-4) ")
        try:
            num_players = int(ans)
        except:
            continue

    players = []
    for player_num in range(num_players):
        player_num += 1
        player_name = input(f"Please enter the name of player {player_num}: ")
        players.append(Player(player_num,player_name))
        players[player_num-1].greet()
    
    shuffle_deck(eruptions)
    split_deck(eruptions,players)
    
    players = select_who_goes_first(players)
    
    cards_per_player = [len(player.cards) for player in players]
    
    while len(players) > 1:
        play_round(players)
        cards_per_player = [len(player.cards) for player in players]
        if min(cards_per_player) == 0:
            losers = [index for index, element in enumerate(cards_per_player) if element == 0]
            losers = losers[::-1] # Reversing order so last element in list is deleted before first element in line below.
            for loser in losers: del players[loser]
            
    slow_print(f"{players[0].name} wins!")        
    
    
if __name__ == "__main__":
    main()
