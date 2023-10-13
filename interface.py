from button import Button
class Gamestatus():
    def __init__(self,screen,ai_settings) -> None:
        self.ai_settings=ai_settings
        self.screen=screen
        self.reset_stats()
    def reset_stats(self):
        # self.ship_left=self.ai_settings.ship_limit
        # self.game_over=1
        self.pause=0
        # self.easy=1
        self.page=0
        self.score=0
        # self.reward=0
    def create_button(self,msg,width=200,height=50,size=48,FILLED=True):
        return Button(self.ai_settings,self.screen,msg,width,height,size,FILLED)
    def draw_page(self):
        if self.page==0:
            # pass
            # life=Life(self.screen)
            # life.draw_life(self.ship_left)
            # score_button=self.create_button("score:"+str(self.score),200,50,48,0)
            # score_button.rect.center=(self.ai_settings.screen_width-score_button.rect.width,float(score_button.rect.height)/2)
            # score_button.draw_button(False)
            start_button=self.create_button("Start")
            start_button.rect.center=(50,50)
            start_button.draw_button()
            talent_button=self.create_button("Talent")
            talent_button.rect.center=(50,150)
            talent_button.draw_button()
            config_button=self.create_button("Config")
            config_button.rect.center=(50,250)
            config_button.draw_button()
            save_button=self.create_button("Save")
            save_button.rect.center=(50,350)
            save_button.draw_button()
            quit_button=self.create_button("Quit")
            quit_button.rect.center=(50,450)
            quit_button.draw_button()
    def turn_page(self,mouse_x,mouse_y):
        pass
        # if self.page==0:
        #     if self.play_rect.collidepoint(mouse_x,mouse_y):
        #         self.page+=1
        # elif self.page==1:
        #     if self.easy_rect.collidepoint(mouse_x,mouse_y):
        #         self.easy=1
        #         self.page+=1
        #     elif self.hard_rect.collidepoint(mouse_x,mouse_y):
        #         self.easy=0
        #         self.page+=1
        

        # if self.page==2:
        #     self.game_over=0
            
            

