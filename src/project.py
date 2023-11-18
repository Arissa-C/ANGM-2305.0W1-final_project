import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Color Palette Generator")
    resolution = (1920, 1080)
    screensaver = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    #img_size = (1920, 1200)
    #img_bg = pygame.transform.scale(img, img_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # TODO: Some game logic
        screensaver.fill((255, 255, 255))
        #screensaver.blit(img, (0, 0))
        pygame.display.flip()
    pygame.quit()
 

if __name__ == "__main__":
    main()