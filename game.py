# Simple game

# Import necessary packages
import pygame
import random 

# Initialize pygame modules
pygame.init() 

# Set game screen height and width
screen_width = 1200
screen_height = 780
screen = pygame.display.set_mode((screen_width, screen_height))

# Create player, enemies and prize objects 
player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("dino.gif")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

# Get width and height of images to test in relevance to screen
image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("Height of player image: " +str(image_height))
print("Width of player image: " +str(image_width))
print("Height of enemy #1 image: " +str(enemy1_height))
print("Width of enemy #1 image: " +str(enemy1_width))
print("Height of enemy #2 image: " +str(enemy2_height))
print("Width of enemy #2 image: " +str(enemy2_width))
print("Height of enemy #3 image: " +str(enemy3_height))
print("Width of enemy #3 image: " +str(enemy3_width))
print("Height of prize image: " +str(prize_height))
print("Width of prize image: " +str(prize_width))

# Resize images to better fit screen
new_player_width = 180
player_width_ratio = new_player_width/image_width
new_player_height = player_width_ratio*image_height
player = pygame.transform.scale(player, (int(new_player_width), int(new_player_height)))

new_enemy1_width = 180
enemy1_width_ratio = new_enemy1_width/enemy1_width
new_enemy1_height = enemy1_width_ratio*enemy1_height
enemy1 = pygame.transform.scale(enemy1, (int(new_enemy1_width), int(new_enemy1_height)))

new_enemy2_width = 180
enemy2_width_ratio = new_enemy2_width/enemy2_width
new_enemy2_height = enemy2_width_ratio*enemy2_height
enemy2 = pygame.transform.scale(enemy2, (int(new_enemy2_width), int(new_enemy2_height)))

new_enemy3_width = 180
enemy3_width_ratio = new_enemy3_width/enemy3_width
new_enemy3_height = enemy3_width_ratio*enemy3_height
enemy3 = pygame.transform.scale(enemy3, (int(new_enemy3_width), int(new_enemy3_height)))

new_prize_width = 180
prize_width_ratio = new_prize_width/prize_width
new_prize_height = prize_width_ratio*prize_height
prize = pygame.transform.scale(prize, (int(new_prize_width), int(new_prize_height)))

# Get width and height of new images in order to do boundary detection
image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("Height of player image: " +str(image_height))
print("Width of player image: " +str(image_width))
print("Height of enemy #1 image: " +str(enemy1_height))
print("Width of enemy #1 image: " +str(enemy1_width))
print("Height of enemy #2 image: " +str(enemy2_height))
print("Width of enemy #2 image: " +str(enemy2_width))
print("Height of enemy #3 image: " +str(enemy3_height))
print("Width of enemy #3 image: " +str(enemy3_width))
print("Height of prize image: " +str(prize_height))
print("Width of prize image: " +str(prize_width))

# Store position of player as variables
playerXPosition = 500
playerYPosition = 500

# Make the enemies start off screen at random y position
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition =  0
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

# Make the prize start off screen at random x position
prizeXPosition =  random.randint(0, screen_width - prize_width)
prizeYPosition =  0

# Check if down, up, left or right key is pressed
# Right now they are not so set to False

keyUp= False
keyDown = False
keyRight = False
keyLeft = False

# This is the game loop
# The game logic needs to be run over and over again
# The screen window must be updated and changes applied to represent real time game play 

while 1: # Looping structure that will loop intended code until quitting 

    screen.fill(0) # Clear screen
    # Make objects start at positions stored in position variables specified earlier
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# Update screen 
    
    # Loop through events in game
    for event in pygame.event.get():
    
        # If user quits program then exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # Check if key pressed is down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # Check if key pressed is up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # Check key pressed and move player accordingly
    
    # The coordinate system of the game window is that the top left corner is (0, 0)
    
    if keyUp == True:
        if playerYPosition > 0 : # Make sure user does not move player above window
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# Make sure user does not move the player below window
            playerYPosition += 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width: # Make sure user does not move player out of window to the left
            playerXPosition += 1
    if keyLeft == True:
        if playerXPosition > 0: # Make sure user does not move player out of window to the right
            playerXPosition -= 1
    
    # Check for collision of enemies with player:
    
    # Bounding box for player:
    playerBox = pygame.Rect(player.get_rect())
    
    # Update playerBox position to player's position
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for enemies and prize:
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test for collision of boxes:
    #If collision with an enemy occurs then user loses game
    #If collision with prize occurs then user wins game
    if playerBox.colliderect(enemy1Box):
        # Display losing status to user: 
        print("You lose!")
        # Quite game and exit window: 
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemy2Box):
        # Display losing status to user: 
        print("You lose!")
        # Quite game and exit window: 
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemy3Box):
        # Display losing status to user: 
        print("You lose!")
        # Quite game and exit window: 
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(prizeBox):
        # Display losing status to user: 
        print("You win!")
        # Quite game and exit window: 
        pygame.quit()
        exit(0)
        
    # If enemies are off the screen without a collision occuring then user wins the game:
    if (enemy1XPosition < 0 - enemy1_width and enemy2XPosition > screen_width and enemy3XPosition < 0 - enemy3_width):
        # Display wining status to user: 
        print("You win!")
        # Quite game and exit window: 
        pygame.quit()
        exit(0)
    
    # Make enemies and prize approach player
    enemy1XPosition -= 0.15
    enemy2XPosition += 0.15
    enemy3XPosition -= 0.15
    prizeYPosition += 0.15
    
    # ================The game loop logic ends here. =============
  



























