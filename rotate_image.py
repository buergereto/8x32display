# coding=utf-8

# provides operating system-dependent functionality
import os

# imports the Pygame library
import pygame

# colors
black = (0, 0, 0)


def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    window_title = u'Rotate image'
    pygame.display.set_caption(window_title)

    # sets the window size
    window_size = (400, 400)
    screen = pygame.display.set_mode(window_size)

    # gets the rectangle that the screen occupies
    screen_rect = screen.get_rect()

    # gets the center of the screen
    screen_center = screen_rect.center

    # loads an image
    image = pygame.image.load(os.path.join('images', 'pygame_logo.png'))

    # converts the image to the same format as the screen to draw it faster
    image = image.convert_alpha()

    # rotation angle
    rotation_angle = 45

    # creates a clock
    clock = pygame.time.Clock()

    # is the application running?
    is_running = True

    # if the application is running
    while is_running:
        # limits updates to 30 frames per second (FPS)
        clock.tick(30)

        # gets all events from the event queue
        for event in pygame.event.get():
            # if the 'close' button of the window is pressed
            if event.type == pygame.QUIT:
                # stops the application
                is_running = False

            # if any key is pressed
            if event.type == pygame.KEYDOWN:
                # if the 'space' key is pressed
                if event.key == pygame.K_SPACE:
                    # rotates the image 45 degrees
                    image = pygame.transform.rotate(image, rotation_angle)

                    # prints on the console the image dimensions
                    print u'image dimensions: {} '.format(image.get_rect())

        # gets the rectangle that occupies the image
        img_rect = image.get_rect()

        # centers the rectangle that occupies the image in the center of the screen
        img_rect.center = screen_center

        # sets the background color
        screen.fill(black)

        # draws the image on the center of the screen
        screen.blit(image, img_rect)

        # updates the screen
        pygame.display.flip()

    # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
