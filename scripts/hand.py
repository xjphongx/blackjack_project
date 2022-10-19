from scripts.placement import Placement
class Hand():
    def __init__(self, order,x ,y, isDealer = False): #add bet size when creating a hand, minimum bet
        self.order = order #the hand's order
        self.x, self.y = x, y
        self.placement = Placement(x,y)
        self.isDealer = isDealer
        self.card_list = []
        self.min_bet = 50
        self.hasAce = False
        self.hand_sum = 0
        self.hand_upper_sum = 0 #calculated for ace edge case
        self.hand_size = 0
        self.player_action_menu = [] #LOOK AT TUTORIAL
        #need to add a small menu containing buttons for player to press 
    
    #function display updates the pygame game display with cards
    def display(self, display):
        
        for i, card in enumerate(self.card_list):
            card.rect = card.image_surface.get_rect(center= (card.x,card.y)) #changes the center
            display.blit(card.image_surface, card.rect)
            if card.x != self.placement.x and card.y != self.placement.y:
                card.x-=10 
                card.y+=10

    
    #print out on terminal the contains of the card_list
    def show(self):
        for i, card in enumerate(self.card_list) :
            print(card.type, end= " ")  
        print()  
    
    #reset hand total sum to zero
    def reset_hand_sum(self):
        self.hand_sum = 0

    #when adding cards to my hand, add pip value as well
    def add_card(self, card): 
        #set hand_sum to be the lower sum and hand uppper is uppper sum
        if card.type == 'Ace':
            self.hasAce = True
            self.hand_sum += card.low_pip_value
            self.hand_upper_sum += card.high_pip_value
        else:
            self.hand_sum += card.pip_value
            self.hand_upper_sum += card.pip_value
        self.card_list.append(card) 
        self.hand_size+=1       #increase hand size when adding a card
        
    def remove_card(self):
        self.hand_sum -= self.card_list[-1].pip_value
        temp_card = self.card_list.pop()
        self.hand_size = len(self.card_list) #update hand size after pop, to prevent error
        return temp_card
         




        
    
