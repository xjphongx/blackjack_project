import pygame
from scripts.player import Dealer,Player
from scripts.stack import DeckPile, DiscardPile

## game board will have the deal and all the players
## contain a stack of cards 

class GameBoard():
    def __init__(self,game):
        print("game board started")
        self.game = game
        self.dealer = Dealer()
        self.deck_pile = DeckPile()
        self.discard_pile = DiscardPile()


    #load json png cards into the deck
    def load_cards_to_deck(self):
        pass
    #Function display_gameboard() displays all gameboard objects
    def display_gameboard(self):
        #set up dealer
        self.game.screen.blit(self.game.gameboard.dealer.dealer_image_surface, self.game.gameboard.dealer.rect)           
        #set up deck
        self.game.screen.blit(self.game.gameboard.deck_pile.deck_back_image_surface, self.game.gameboard.deck_pile.rect) 
        #set up discard pile
        self.game.screen.blit(self.game.gameboard.discard_pile.discard_pile_image_surface, self.game.gameboard.discard_pile.rect)
        #set up player 
            #set up player's hands
        #start turn system
        
        
    def check_input(self):
        pass
    


        

