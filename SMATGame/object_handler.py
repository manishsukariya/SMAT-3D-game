from sprite import *
from npc import * 


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/npc/pain/'
        self.static_sprite_path = 'resources/sprite/fire/'
        self.anim_sprite_path = 'resources/sprite/fire/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}
        
        # Add sprites
        self.add_sprite(SpriteObject(game))
        self.add_sprite(AnimatedSprite(game))
        self.add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        self.add_sprite(AnimatedSprite(game, pos=(1.5, 18.5)))
        self.add_sprite(AnimatedSprite(game, pos=(23.5, 1.5)))
        self.add_sprite(AnimatedSprite(game, pos=(23.5, 18.5)))

        # npc map
        
        add_npc(NPC(game, pos=(10.5, 10.5)))#1
        add_npc(NPC(game, pos=(1.5, 9.5)))#2
        add_npc(NPC(game, pos=(6.5, 17.5)))#3
        add_npc(NPC(game, pos=(6.5, 18.5)))#4
        add_npc(NPC(game, pos=(4.5, 11.5)))#5
        add_npc(NPC(game, pos=(2.5, 6.5)))#6
        add_npc(NPC(game, pos=(5.5, 4.5)))#7
        add_npc(NPC(game, pos=(13.5, 1.5)))#8
        add_npc(NPC(game, pos=(23.5, 8.5)))#9
        add_npc(NPC(game, pos=(23.5, 10.5)))#10
        add_npc(NPC(game, pos=(21.5, 14.5)))#11
        add_npc(NPC(game, pos=(21.5, 15.5)))#12
        add_npc(NPC(game, pos=(11.5, 18.5)))#13
        add_npc(NPC(game, pos=(13.5, 18.5)))#14
        add_npc(NPC(game, pos=(11.5, 1.5)))#15
        add_npc(NPC(game, pos=(19.5, 14.5)))#16
        add_npc(NPC(game, pos=(19.5, 15.5)))#17'''
        add_npc(NPC(game, pos=(20.5, 14.5)))#18
        add_npc(NPC(game, pos=(20.5, 15.5)))#19
        add_npc(NPC(game, pos=(19.5, 12.5)))#20
        add_npc(NPC(game, pos=(19.5, 13.5)))#21
        add_npc(NPC(game, pos=(18.5, 12.5)))#22
        add_npc(NPC(game, pos=(18.5, 13.5)))#23
        add_npc(NPC(game, pos=(15.5, 9.5)))#24
        add_npc(NPC(game, pos=(15.5, 10.5)))#25
        add_npc(NPC(game, pos=(15.5, 11.5)))#26
        add_npc(NPC(game, pos=(15.5, 12.5)))#27
        add_npc(NPC(game, pos=(15.5, 13.5)))#28
        add_npc(NPC(game, pos=(15.5, 14.5)))#29
        add_npc(NPC(game, pos=(17.5, 5.5)))#30
        

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
