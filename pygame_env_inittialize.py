import pygame

class GameEngineInit:
    win = None

    def __init__(self, size, caption:str):
        pygame.init()
        self.win = pygame.display.set_mode(size=size)
        pygame.display.set_caption(caption)

        self.return_obj()

    def return_obj(self):
        return (pygame, self.win)
