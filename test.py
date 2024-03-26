import pygame

# Activate the pygame library.
# Initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# Create the display surface object
# of specific dimension (500, 500).
win = pygame.display.set_mode((2000, 2000))

# Set the pygame window name.
pygame.display.set_caption("Jump Game")

# Load the image for the player
player_img = pygame.image.load('1.gif')  # Replace 'player.png' with your image file path

# Object current coordinates
x = 0
y = 0

# Stores if player is jumping or not
isjump = False

# Force (v) up and mass m.
v = 10
m = 1

# Indicates pygame is running
run = True

# Infinite loop
while run:
    win.fill((0, 0, 0))

    # Completely fill the surface object
    # with black color

    # Drawing object on screen which is a player image
    win.blit(player_img, (x, y))

    # Iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # If event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # It will make exit the while loop
            run = False

    # Stores keys pressed
    keys = pygame.key.get_pressed()

    if isjump == False:

        # If space bar is pressed
        if keys[pygame.K_SPACE]:
            # Make isjump equal to True
            isjump = True

    if isjump:
        # Calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F = (1 / 2) * m * (v ** 2)

        # Change in the y-coordinate
        y -= F

        # Decreasing velocity while going up and become negative while coming down
        v = v - 1

        # Object reached its maximum height
        if v < 0:
            # Negative sign is added to counter negative velocity
            m = -1

        # Object reached its original state
        if v == -11:
            # Making isjump equal to False
            isjump = False

            # Setting original values to v and m
            v = 10
            m = 1

    # Creates time delay of 10ms
    pygame.time.delay(10)

    # It refreshes the window
    pygame.display.update()
# Closes the pygame window
pygame.quit()
