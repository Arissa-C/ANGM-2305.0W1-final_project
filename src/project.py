import pygame
import math
import pygame_gui

from pygame_gui.elements import UIButton

def main():
    pygame.init()
    pygame.display.set_caption("Color Palette Generator")
    resolution = (1920, 1080)
    screensaver = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    col_pick = ColorWheel(250, 150, 300, 350)
    hsl_graph = HSLGraph(850, 150, 375, 375, col_pick)
    #img_size = (1920, 1200)
    #img_bg = pygame.transform.scale(img, img_size)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        col_pick.update()
        hsl_graph.draw(screensaver)
        
        screensaver.fill((49, 51, 53))
        hsl_graph.draw(screensaver)
        col_pick.draw(screensaver)
        #screensaver.blit(img, (0, 0))
        pygame.display.flip()
    pygame.quit()
 

class ColorWheel():

    def __init__(self, x, y, width, height, radius= 50):
        self.x = x
        self.y = y
        self.image = pygame.Surface((2 * width, 2 * height))
        self.image.fill((49, 51, 53))
        self.radius = min (width, height) //2
        self.pwidth = min (width, height)
        
        for idx in range(self.pwidth):
            color = pygame.Color(0)
            angle = math.radians(360 * idx / self.pwidth)
            position_x = int(math.cos(angle) * self.radius) + width
            position_y = int(math.sin(angle) * self.radius) + height
            color.hsla = (int(360*idx/self.pwidth), 100, 50, 100)
            pygame.draw.circle(self.image, color, (position_x, position_y), radius)
        
        self.p = 0


    def get_colors(self):
        color = pygame.Color(0)
        color.hsla = (int((self.p * 360) % 360), 100, 50, 100)
        return color


    def update(self):
        #TODO: fix mouse inputs
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_position = pygame.mouse.get_pos()

        wheel_mid = (self.x, self.y)
        dist = math.sqrt((mouse_position[0] - wheel_mid[0]) ** 2 + (mouse_position[1] - wheel_mid[1]) **2)

        if dist <= self.radius:
            angle = math.atan2(mouse_position[1]-wheel_mid[1], mouse_position[0]-wheel_mid[0])
            pos_x = int(math.cos(angle) * self.radius) + self.x
            pos_y = int(math.sin(angle) * self.radius) + self.y
            self.p = (dist - self.image.get_rect(center = wheel_mid).left - self.radius) / self.pwidth
            


    def draw(self, surf):
        draw_x = self.x - self.radius
        draw_y = self.y - self.radius
        surf.blit(self.image, (draw_x, draw_y))
        cent = self.x - draw_x, self.y - draw_y
        pygame.draw.circle(surf, self.get_colors(), cent, self.radius // 2)


class HSLGraph():

    def __init__(self, x, y, width, height, picked_colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.picked_colour = picked_colour
        self.hslsurf = pygame.Surface((width, height))
        
    
    def update_hslgraph(self):
        self.hslsurf.fill((0, 0, 0))

        if self.picked_colour:
            chosen_col = self.picked_colour.get_colors()
            pixs = pygame.PixelArray(self.hslsurf)
    
            for x in range (self.width):
               for y in range(self.height):
                sat = x / self.width * 100
                lum = (1-y / self.height) * 100

                colours = pygame.Color(0)
                colours.hsla = (chosen_col.hsla[0], sat, lum, 100)

                pixs[x, y] = colours
        
            del pixs

    def draw(self, surf):
        self.update_hslgraph()
        surf.blit(self.hslsurf, (self.x, self.y))

if __name__ == "__main__":
    main()