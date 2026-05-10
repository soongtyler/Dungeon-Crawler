import pygame
from gameobject import *
from wall import Wall

GREEN  = (0, 255, 0)

class Player(GameObject):
    def __init__(self, gridx, gridy, tile_width, tile_height, color = GREEN):
        # Calculate the initial pos manually using grid system tiles
        x = gridx * tile_width
        y = gridy * tile_height
        super().__init__(gridx, gridy, x, y, tile_width, tile_height, color)

    def draw(self, surface):
        ## TODO: need to update
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.tile_width, self.tile_height))

    def handle_input(self, event, game_map, tile_cols, tile_rows):
        # create a bool var to act as flag to return later whether or not we moved
        moved = False

        new_gridx = self.gridx
        new_gridy = self.gridy

        # detect key down
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                ## move up
                new_gridy -= 1

            elif event.key in (pygame.K_DOWN,pygame.K_s):
                # move down
                new_gridy += 1

            elif event.key in (pygame.K_LEFT, pygame.K_a):
                # move left
                new_gridx -= 1

            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                # move right
                new_gridx += 1

        ##  check boundary
        if new_gridx >= 0 and new_gridx < tile_cols and new_gridy >= 0 and new_gridy < tile_rows:
            if game_map[new_gridx][new_gridy] == 0:
                # Update the new position and clear the previous one on the map for the player
                    game_map[new_gridy][new_gridx] = game_map[self.gridy][self.gridx]
                    game_map[self.gridy][self.gridx] = 0

                    self.gridx = new_gridx
                    self.gridy = new_gridy
                    moved = True

        return moved

    def update(self):
        
        pass
        
        # update position
        self.x = self.gridx * self.tile_width
        self.y = self.gridy * self.tile_height