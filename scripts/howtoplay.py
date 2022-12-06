import pygame
from scripts.state import State
from scripts.button import Button

class Tutorial(State):
    def __init__(self, game):
        super().__init__(game)
        self.back_x = 150
        self.back_y = 55
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, .10)
        next_image = pygame.image.load("images/buttons/next_button.png").convert_alpha()
        self.next_button = Button(game.display_width-self.back_x, self.back_y, next_image, .10)

    def render(self,display):
        display.fill(self.game.background_color)
        self.game.draw_text('How to Play', 100, self.game.display_width/2, self.game.display_height/10)
        #TODO - add text instructions 
        #TODO - add image instructions
        #TODO - think about adding multiple pages/states
        #render the clickable buttons
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True
        elif self.next_button.draw(self.game.display):
            self.game.actions["next"] = True
            
    def update(self,actions):
        #goes back to previous state by exiting current state
        if actions["back"]:
            self.exit_state()
        elif actions["next"]:
            next_state = Tutorial_2(self.game)
            next_state.enter_state()
            
        self.game.reset_actions()

class Tutorial_2(State):
    def __init__(self, game):
        super().__init__(game)
        self.back_x = 150
        self.back_y = 55
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(self.back_x, self.back_y, back_image, .10)

    def render(self,display):
        display.fill(self.game.background_color)
        self.game.draw_text('How to Play', 100, self.game.display_width/2, self.game.display_height/10)
        if self.back_button.draw(self.game.display):
            self.game.actions["back"] = True
    
    def update(self,actions):
        if actions["back"]:
            self.exit_state()
            self.prev_state.enter_state() #go to the previous state(tutorial 1)
        self.game.reset_actions()