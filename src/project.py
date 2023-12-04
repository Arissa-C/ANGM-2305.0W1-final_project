import pygame
import math
import pygame_gui


from pygame_gui.elements import UIButton
from pygame_gui.elements import UILabel

def main():
    pygame.init()
    pygame.display.set_caption("Color Palette Generator")
    resolution = (1920, 1080)
    screensaver = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    ui_manager = pygame_gui.UIManager(resolution)
    col_pick = ColorWheel(200, 110, 300, 350, ui_manager)
    hsl_graph = HSLGraph(750, 125, 375, 375, col_pick, ui_manager)
    adding_button = UIButton(relative_rect=pygame.Rect(1100, 600, 145, 35),
                                     text='Add to Palette',
                                     manager= ui_manager)
    subtract_button = UIButton(relative_rect=pygame.Rect(1080, 665, 180, 35),
                               text = "Remove from Palette", 
                               manager=ui_manager)
    col_pal = ColorPalette(250, 565, 145, 145, col_pick, hsl_graph, ui_manager, adding_button, subtract_button)
    hsl_graph.create_sliders()
    hsl_graph.add_labels()
    col_pick.add_wheel_title()
    col_pal.add_title()
    running = True
    while running:
        time_delta = clock.tick(60) // 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            ui_manager.process_events(event)
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == adding_button:
                    col_pal.adding_squares()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == subtract_button:
                    col_pal.subtract_squares()
            
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                col_pal.add_mouse_selector()

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                col_pick.mouse_cursor()

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP or event.type==pygame.MOUSEMOTION:
                hsl_graph.add_mouse_input()


        col_pick.mouse_cursor()
        ui_manager.update(time_delta)
        screensaver.fill((25, 25, 25))
        hsl_graph.update_hslgraph()
        hsl_graph.draw(screensaver)
        col_pick.draw(screensaver)
        col_pal.draw(screensaver)
        ui_manager.draw_ui(screensaver)
        pygame.display.flip()
    pygame.quit()
 

class ColorWheel():

    def __init__(self, x, y, width, height, ui_manager, radius= 50):
        self.x = x 
        self.y = y 
        self.image = pygame.Surface((2 * width, 2 * height)) 
        self.image.fill((25, 25, 25))
        self.radius = min (width, height) //2 
        self.pwidth = min (width, height)
        self.mouse_press = False
        self.ui_manager = ui_manager 
        
        for idx in range(self.pwidth):
            color = pygame.Color(0) 
            angle = math.radians(360 * idx / self.pwidth) 
            position_x = int(math.cos(angle) * self.radius) + width 
            position_y = int(math.sin(angle) * self.radius) + height 
            color.hsla = (int(360*idx/self.pwidth), 100, 50, 100) 
            pygame.draw.circle(self.image, color, (position_x, position_y), radius)
        
        self.p = 0

    def add_wheel_title(self):
        self.wheel_title = UILabel(relative_rect=pygame.Rect(100, 30, 300, 150), text="Color Wheel",
                                         manager=self.ui_manager)

    def get_colors(self):
        color = pygame.Color(0)
        color.hsla = (int((self.p * 360) % 360), 100, 50, 100)
        return color
    

    def mouse_cursor(self):
        mouse_button = pygame.mouse.get_pressed()
        mouse_position = pygame.mouse.get_pos()

        if mouse_button [0]:
            distance_x = mouse_position[0] - (self.x + self.radius)
            distance_y = mouse_position[1] - (self.y + self.radius)
            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
            if distance > 0 and distance <= self.radius:
               angel= math.atan2(distance_y, distance_x) 
               angel_ran= (angel % (2 * math.pi))
               angel_fraction = angel_ran / (2 * math.pi)
               self.p = angel_fraction
     
    def draw(self, surf):
        self.mouse_cursor()
        mouse_x = int(math.cos(self.p * 2 * math.pi) * self.radius) + self.x * 1.85
        mouse_y = int(math.sin(self.p * 2 * math.pi) * self.radius) + self.y * 2.85
        draw_x = self.x - self.radius
        draw_y = self.y - self.radius
        surf.blit(self.image, (draw_x, draw_y))
        pygame.draw.circle(surf, (0, 0, 0), (mouse_x, mouse_y), self.radius // 5)
        pygame.draw.circle(surf, self.get_colors(), (mouse_x, mouse_y), self.radius // 7)


class HSLGraph():

    def __init__(self, x, y, width, height, picked_colour, ui_manager):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.picked_colour = picked_colour
        self.hslsurf = pygame.Surface((width, height))
        self.sat_slider = None
        self.sat_value = 100.0
        self.lum_slider = None
        self.lum_value = 100.0
        self.ui_manager= ui_manager
        self.sat_slider_label = None
        self.lum_slider_label = None

    def create_sliders(self):
        self.sat_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(925, 500, 200, 25),
                                                                 start_value= self.sat_value, value_range=(0.0 , self.sat_value),
                                                                 manager=self.ui_manager, object_id= 'Saturation')
        self.lum_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect(925, 530, 200, 25),
                                                                 start_value= self.lum_value, value_range=(0.0, self.lum_value),
                                                                 manager=self.ui_manager, object_id= 'Luminosity')
        
    def add_labels(self):
        self.title_label = UILabel(relative_rect=pygame.Rect(720, 30, 300, 150), text="Saturation & Luminosity Graph",
                                         manager=self.ui_manager)
        self.sat_slider_label = UILabel(relative_rect=pygame.Rect(740, 496, 180, 30),
                                    text="Saturation Control", manager=self.ui_manager)
        self.lum_slider_label = UILabel(relative_rect=pygame.Rect(740, 530, 180, 30),
                                   text="Luminosity Control", manager=self.ui_manager)
        self.percent_sat_label = UILabel(relative_rect=pygame.Rect(1055, 500, 180, 20), text="100%",
                                         manager=self.ui_manager)
        self.percent_lum_label = UILabel(relative_rect=pygame.Rect(1055, 530, 180, 20), text="100%",
                                         manager=self.ui_manager)
        self.zero_perc_sat_lab = UILabel(relative_rect=pygame.Rect(825, 496, 180, 30), text="0%",
                                         manager=self.ui_manager)
        self.zero_perc_lum_lab = UILabel(relative_rect=pygame.Rect(825, 528, 180, 30), text="0%",
                                         manager=self.ui_manager)

    def add_mouse_input(self):
        mouse_butt = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_butt [0] and self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
                graph_x = (mouse_pos[0] - self.x) / self.width
                graph_y = (mouse_pos[1] - self.y) / self.height
                self.sat_slider.set_current_value(graph_x * 100)
                self.lum_slider.set_current_value((1 - graph_y) * 100)

                                                                     
    def update_hslgraph(self):
        if self.sat_slider:
            self.sat_value = self.sat_slider.get_current_value()
        if self.lum_slider:
            self.lum_value = self.lum_slider.get_current_value()

        self.hslsurf.fill((0, 0, 0))
        if self.picked_colour:
            chosen_col = self.picked_colour.get_colors()
            pixs = pygame.PixelArray(self.hslsurf)
    
            for x in range (self.width):
               for y in range(self.height):
                sat = x / self.width * self.sat_value
                lum = (1 - y / self.height) * self.lum_value

                colours = pygame.Color(0)
                colours.hsla = (chosen_col.hsla[0], sat, lum, 100)

                pixs[x, y] = colours
        
            del pixs


    def draw(self, surf):
        self.update_hslgraph()
        surf.blit(self.hslsurf, (self.x, self.y))
        if self.sat_slider:
            self.ui_manager.draw_ui(surf)
        if self.lum_slider:
            self.ui_manager.draw_ui(surf)
        


class ColorPalette():


    def __init__(self, x, y, width, height, selected_color, hsl_graph, ui_manager, adding_button, subtract_button):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected_color = selected_color
        self.squares = [pygame.Surface((width, height)) for _ in range(5)]
        self.hsl_graph = hsl_graph
        self.ui_manager = ui_manager
        self.adding_button = adding_button
        self.subtract_button = subtract_button
        self.selected_sq = None
 
    def add_title(self):
        self.palette_title = UILabel(relative_rect=pygame.Rect(155, 480, 300, 150), text="Color Palette",
                                         manager=self.ui_manager)


    def adding_squares(self):
        if len(self.squares) < 5:
          self.squares.append(pygame.Surface((self.width, self.height)))
        elif len(self.squares) == 5:
           self.button_display()

    def subtract_squares(self):
        if len(self.squares) > 1:
            self.squares.pop()
        elif len(self.squares) <= 5:
            self.button_display()

    def button_display(self):
        if len(self.squares) < 5:
            self.adding_button.show()
        else:
            self.adding_button.hide()
        
        if len(self.squares) > 1:
            self.subtract_button.show()
        else:
            self.subtract_button.hide()

    def add_mouse_selector(self):
        mouse_pad = pygame.mouse.get_pressed()
        mouse_loc = pygame.mouse.get_pos()
        
        if mouse_pad[0]:
            for numb, sq_surface in enumerate(self.squares):
                sq_x = self.x + numb * (self.width + 10)
                sq_rect = pygame.Rect(sq_x, self.y, self.width, self.height)

                if sq_rect.collidepoint(mouse_loc):
                    self.selected_sq = numb
                    return
  
    def change_colours(self):
        if self.selected_sq is not None and 0 <= self.selected_sq < len(self.squares):
            sel_color = self.selected_color.get_colors()
            saturated = self.hsl_graph.sat_slider.get_current_value()
            brightness = self.hsl_graph.lum_slider.get_current_value()
            sel_color.hsla = (sel_color.hsla[0], saturated, brightness, 100)
            self.squares[self.selected_sq].fill(sel_color)
            
    def draw(self, surf):
        self.button_display()
        self.change_colours()
        for num, sq_surf in enumerate(self.squares):
            draw_x = self.x + num * (self.width + 10)
            surf.blit(sq_surf, (draw_x, self.y))
            if num == self.selected_sq:
                pygame.draw.rect(surf, (137, 207, 240), (draw_x, self.y, self.width, self.height), 4)

                            
if __name__ == "__main__":
    main()