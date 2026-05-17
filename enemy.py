import pygame
import random
from gameobject import GameObject

#Constants
RED = (255,0,0)

class Enemy(GameObject):
    def __init__(self, gridx, gridy, tile_width, tile_height, color=RED):
        #Calculate the initial position manually using grid system tiles
        x = gridx * tile_width
        y = gridy * tile_height
        super().__init__(gridx, gridy, x, y, tile_width, tile_height, color)


    def draw(self, surface):
        # TODO: the enemy will start out as a rect but we will update this later on
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.tile_width, self.tile_height))


    def update(self):
        # Always update the actual x and y position on the pygame displayed based on our grid tiles
        self.x = self.gridx * self.tile_width
        self.y = self.gridy * self.tile_height

    def take_turn(self, game_map, tile_cols, tile_rows):
        #Enemy takes a turn
        self._move_random_adjacent(game_map, tile_cols, tile_rows)


    def _move_random_adjacent(self, game_map, tile_cols, tile_rows):
        
        #Create list of direction options for the enemy
        directions = [(0, -1),#move down
                      (0, 1),#move up
                      (-1, 0),#move left
                      (1, 0)]#move right
        
        #Shuffle the direction list
        random.shuffle(directions)

        #Iterate through the direction tuple list, move on the first one that is

        for dx, dy in directions:
            new_gridx = self.gridx + dx
            new_gridy = self.gridy + dy

            #Check within boundaries
            if 0 <= new_gridx < tile_rows and 0 <= new_gridy < tile_cols:
                if game_map[new_gridx][new_gridy] == 0:
                    # Update the new position and clear the previous one on the map

                    game_map[new_gridx][new_gridy] = game_map[self.gridx][self.gridy]
                    game_map[self.gridx][self.gridy] = 0
                    self.gridx = new_gridx
                    self.gridy = new_gridy
                    break



