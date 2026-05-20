import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.npc_shot = pg.mixer.Sound(self.path + 'npcshot.mp3')
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.mp3')
        self.win = pg.mixer.Sound(self.path + 'win.mp3')
        self.lose = pg.mixer.Sound(self.path + 'lose1.mp3')
        self.game_over = pg.mixer.Sound(self.path + 'game_over1.mp3')
        
