
import pygame
from scripts.bet_menu import Bet_Menu
from scripts.cursor import Cursor
from scripts.hand import Hand
from scripts.player import Dealer, Player
from scripts.ring_row import Ring_Row
from scripts.stack import DeckPile, DiscardPile
from scripts.state import State
from scripts.button import Button

class Gameboard(State):
    def __init__(self, game):
        super().__init__(game)
        #instantiating gameboard objects
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(325, 50, back_image, self.game.IMAGE_SCALE)
        self.dealer = Dealer()
        self.deck_pile = DeckPile()
        self.deck_pile.load_cards_to_deck()
        self.discard_pile = DiscardPile()
        for i in range(8):     #shuffle the deck when starting the gameboard
            self.deck_pile.cut_deck()
            self.deck_pile.casino_shuffle()          
        #temporary button
        confirm_button_image = pygame.image.load("images/buttons/confirm_button.png").convert_alpha()
        self.confirm_button = Button(self.game.display_width/2, self.game.display_height/2, confirm_button_image,scale=.1)
        #intialize ring row
        self.ring_row = Ring_Row(self.game, self) #self.game,
        #intialize bet menu
        self.bet_menu = Bet_Menu(self.game, self)
        #intialize cursor object 
        self.cursor = Cursor(self.game) 

        self.player = Player()
        #turn list
        self.turn_list = []
        
    def render(self,display):
        display.fill(self.game.background_color)
        #set up dealer
        self.game.draw_text("Dealer", 30, self.game.display_width/2,125)
        self.game.display.blit(self.dealer.dealer_image_surface, self.dealer.rect)           
        #set up deck
        self.game.display.blit(self.deck_pile.deck_back_image_surface, self.deck_pile.rect) 
        #set up discard pile
        self.game.display.blit(self.discard_pile.discard_pile_image_surface, self.discard_pile.rect)
        #self.game.draw_text('Playing game', 100, self.game.display_width/2,self.game.display_height/10)            
        self.game.draw_text("How many hands are you playing?", 50, self.game.display_width/2,self.game.display_height/5)
        #betting bar and functionality
        self.bet_menu.display()
        #hand ring functionality
        self.ring_row.display()

        #checks if player is deciding, if clicked, pass out cards
        if self.confirm_button.isActive == False: 
                #if player clicks the confirm button and the row is empty, do nothing
                if self.ring_row.isEmpty == True :
                    self.confirm_button.draw(self.game.display) #still display the button
                #if player places a bet, confirm and play the game
                elif self.ring_row.isEmpty == False: 
                    if self.confirm_button.draw(self.game.display): #figure out how to clear this button
                     #hand list is not empty or ring row is empty
                        #combine the player and dealer hands, player goes first
                        self.turn_list.extend(self.dealer.hand_list)
                        self.turn_list.extend(self.player.hand_list)
                        self.confirm_button.isActive = True #removes the confirm button from screen
                        #self.game.display.blit(self.hand_1_button.image,(self.confirm_button.rect.x,self.confirm_button.rect.y))
                        #print(f"Player's Hand {self.player.hand_list}")
                        #print(f"Dealer's Hand {self.dealer.hand_list}")
                        #print(f"Turn list {self.turn_list}")

                        self.filter_List()
                        #print(f"After filter Turn list {self.turn_list}")

                        #start the blackjack game
                        self.play()






        #render the clickable button
        if self.back_button.draw(self.game.display):
            self.ring_row.clear() #clears the row 
            self.game.actions["back"] = True

    #state change to the title
    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()

    #function filter list uses a simple algorithm to search and replace the list
    def filter_List(self):
        temp_list = []   #temperary list to contain hand objects     
        for i, hand in enumerate(self.turn_list): #cycles and gets the hand 
            if isinstance(hand, Hand): #test if hand is a hand object
                temp_list.append(hand)

        self.turn_list = temp_list.copy() #turn list is replaced with the filtered lsit
        temp_list.clear()
        



    def play(self):
        print("playing blackjack")
        #intial passing of cards to each hand and dealer, only passes out 2 cards
        #this algorithm passes out cards in circle order from hand 1 - 5 and dealer's hand
        for rotation in range(2):
            for i, hand in enumerate(self.turn_list):
                top_card = self.deck_pile.top()
                self.deck_pile.pop()
                hand.add_card(top_card)

        self.printTest()   

        
             
        





    def printTest(self):
            #loop through all the hands to test print
        for i, hand in enumerate(self.turn_list):
            #loop through the cards in THAT specific hand
            print(f"hand {hand.order}", end = " ")
            for j, card in enumerate(hand.card_list):
                print(hand.card_list[j].type,end = " ")

            #if hand has an Ace card, show two different sum values
            if hand.hasAce:
                print(f"Hand Sum: {hand.hand_sum}")
                print(f"Upper Hand Sum: {hand.hand_upper_sum}")
            else:
                print(f"Hand Sum: {hand.hand_sum}")