import pygame
import os
from gameobject import *
from wall import Wall
from spritesheet import load_spritesheet, Animation

GREEN  = (0, 255, 0)
MOVE_FRAMES = 10

# Path to player sprite assets (relative to this file)
ASSET_DIR = os.path.join(os.path.dirname(__file__), "assets", "1 Pink_Monster")

class Player(GameObject):
    def __init__(self, gridx, gridy, tile_width, tile_height, color = GREEN):
        # Calculate the initial pos manually using grid system tiles
        x = gridx * tile_width
        y = gridy * tile_height
        super().__init__(gridx, gridy, x, y, tile_width, tile_height, color)

        ## Movement animation
        self.move_speed = tile_width/MOVE_FRAMES ## how much distance to cover each frame

        # Sprite animations
        scale = (tile_width, tile_height)
        self.animations = {
            "idle": Animation(load_spritesheet(os.path.join(ASSET_DIR, "Pink_Monster_Idle_4.png"), 
                                               32, 32, scale), speed=8),
            "walk": Animation(load_spritesheet(os.path.join(ASSET_DIR, "Pink_Monster_Walk_6.png"), 
                                               32, 32, scale), speed=max(1, MOVE_FRAMES // 8)),
        }
        self.current_animation = "idle"
        self.direction = "right"
        self.is_moving = False



    def draw(self, surface):
        # ## TODO: need to update
        # pygame.draw.rect(surface, self.color, (self.x, self.y, self.tile_width, self.tile_height))

        frame = self.animations[self.current_animation].get_frame()
        # Flip horizontally when facing left
        if self.direction == "left":
            frame = pygame.transform.flip(frame, True, False)
        surface.blit(frame, (self.x, self.y))



    def handle_input(self, event, game_map, tile_cols, tile_rows):
        # Block new input while still sliding to the target tile
        if self.is_moving:
            return False

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
                self.direction = "left"

            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                # move right
                new_gridx += 1
                self.direction = "right"

        ##  check boundary
        if new_gridx >= 0 and new_gridx < tile_cols and new_gridy >= 0 and new_gridy < tile_rows:
            # self.gridx = new_gridx
            # self.gridy = new_gridy
            # moved = True

            if game_map[new_gridx][new_gridy] == 0:
                ## update the new pos and clear the prev one
                game_map[new_gridx][new_gridx] = game_map[self.gridy][self.gridx]
                game_map[self.gridy][self.gridx] = 0
                self.gridx = new_gridx
                self.gridy = new_gridy
                moved = True

        return moved

    def update(self):
        ## Set target x and y
        target_x = self.gridx * self.tile_width
        target_y = self.gridy * self.tile_height

        # check if we are before or after target x
        if self.x < target_x:
            self.x = min(self.x + self.move_speed, target_x)

        elif self.x > target_x:  
            self.x = max(self.x - self.move_speed, target_x)

        # check if we are before or after target y
        if self.y < target_y:
            self.y = min(self.y + self.move_speed, target_y)
        elif self.y > target_y:
            self.y = max(self.y - self.move_speed, target_y)

        # Determine if still moving and pick the right animation
        self.is_moving = (self.x != target_x or self.y != target_y)

        if self.is_moving:
            if self.current_animation != "walk":
                self.current_animation = "walk"
                self.animations["walk"].reset()
            self.animations["walk"].tick()
        else:
            if self.current_animation != "idle":
                self.current_animation = "idle"
                self.animations["idle"].reset()
            self.animations["idle"].tick()

