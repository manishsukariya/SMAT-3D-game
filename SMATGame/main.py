import pygame as pg
import sys
from settings import *
from SMAT_map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *
from npc import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 100)
        self.state = 'menu'  
        self.show_menu = True
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)

    def update(self):
        if self.state == 'game':  
            self.player.update()
            self.raycasting.update()
            self.object_handler.update()
            self.weapon.update()

        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption("SMATGame")

    def draw(self):
        self.screen.fill('BLACK') 
        if self.state == 'game':
            self.object_renderer.draw()
            self.weapon.draw()
        
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE and self.state == 'menu': 
                self.state = 'game'  
                self.show_menu = False 
            elif event.type == self.global_event:
                self.global_trigger = True
            if self.state == 'game':
                self.player.single_fire_event(event)

    def menu_screen(self):
        bg_image = pg.image.load('resources/start_screen/smat_start.jpg').convert() 

        while self.show_menu:
            self.screen.blit(bg_image, (0, 0)) 
            bg_image = pg.transform.scale(bg_image, RES)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE: 
                    self.show_menu = False 
                    self.state = 'game' 

            pg.display.flip()

    def run(self):
        self.menu_screen()
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
