import sys
import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/sky/sky_100.jpeg', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('resources/bloodscreen/blood_screen.png', RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'resources/digits/{i}.png', [self.digit_size] * 2)
                             for i in range (11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture('resources\game_over/wasted1.png', RES)
        self.victory_image = self.get_texture('resources/victory/victory1.png', RES)
        self.game_over_image_by_quiz = self.get_texture('resources/game_over/game_over1.jpg', RES)
        self.victory = False
        
    def draw(self):
        self.draw_background()
        self.render_game_object()
        self.draw_player_health()
        self.victory_condition()

    def victory_condition(self):
        if all(not npc.alive for npc in self.game.object_handler.npc_list):
            self.victory = True
            self.game.sound.win.play()
            self.game.object_renderer.game_victory()
            pg.display.flip()
            pg.time.delay(6000)
            self.game.__init__()       
            self.game.menu_screen()       

            self.game.sound.win.play()

    def game_victory(self):
        self.screen.blit(self.victory_image, (0, 0))
    
    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def game_over_quiz(self):
        self.screen.blit(self.game_over_image_by_quiz, (0, 0))

    

    def draw_player_health(self):
        health = str(self.game.player.health)
    
        if health.startswith('-'):
            health = '0' 

        for i, char in enumerate(health):
            if char in self.digits:
                self.screen.blit(self.digits[char], (i * self.digit_size, 0))
            else:
                self.screen.blit(self.digits['0'], (i * self.digit_size, 0))

        if int(health) >= 10:
            self.screen.blit(self.digits['10'], ((len(health)) * self.digit_size, 0))


    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_object(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return{
            1: self.get_texture('resources/wall/wall6969.png'),
            2: self.get_texture('resources/wall/wall6969.png'),
            3: self.get_texture('resources/wall/3.jpeg'),
            4: self.get_texture('resources/wall/4.jpeg'),
            5: self.get_texture('resources/wall/5.jpeg'),
            6: self.get_texture('resources/wall/6.jpeg'),
            7: self.get_texture('resources/wall/S.jpg'),
            8: self.get_texture('resources/wall/M.jpg'),
            9: self.get_texture('resources/wall/A.jpg'),
            11: self.get_texture('resources/wall/T.jpg'),
            }



