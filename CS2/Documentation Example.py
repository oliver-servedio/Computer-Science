import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600                     # Set the window dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders") # Set the window title

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define game objects
player_width, player_height = 50, 50         # Set the player dimensions
player_x = WIDTH // 2 - player_width // 2    # Set the initial player x-coordinate
player_y = HEIGHT - player_height - 10       # Set the initial player y-coordinate
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

enemy_width, enemy_height = 40, 40           # Set the enemy dimensions
enemy_list = []                              # Create an empty list to store enemies
for i in range(10):                          # Create 10 enemies
    enemy_x = i * (enemy_width + 10) + 10    # Calculate the x-coordinate for the enemy
    enemy_y = 50                             # Set the initial y-coordinate for the enemy
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    enemy_list.append(enemy_rect)            # Add the enemy to the list

bullet_width, bullet_height = 5, 15          # Set the bullet dimensions
bullet_list = []                             # Create an empty list to store bullets

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        # If the user quits the game
            running = False
        elif event.type == pygame.KEYDOWN:   # If a key is pressed
            if event.key == pygame.K_SPACE:  # If the spacebar is pressed
                bullet_rect = fire_bullet(player_x, player_y, bullet_width, bullet_height)
                bullet_list.append(bullet_rect)

    # Move the player
    keys = pygame.key.get_pressed()          # Get the current state of all keys
    player_x_change = 0                      # Reset the player's horizontal movement
    if keys[pygame.K_LEFT]:                  # If the left arrow key is pressed
        player_x_change = -5                 # Move the player left
    if keys[pygame.K_RIGHT]:                 # If the right arrow key is pressed
        player_x_change = 5                  # Move the player right
    player_x += player_x_change              # Update the player's x-coordinate
    player_rect.x = player_x                 # Update the player's rectangle

    # Move the bullets
    bullet_list = move_bullets(bullet_list)

    # Check for collisions
    enemy_list = check_collisions(enemy_list, bullet_list)

    # Draw objects
    draw_objects(screen, player_rect, enemy_list, bullet_list)

    pygame.display.flip()                    # Update the display

# Quit Pygame
pygame.quit()

def fire_bullet(player_x, player_y, bullet_width, bullet_height):
    """
    Create a new bullet rectangle at the player's position.

    Args:
        player_x (int): The x-coordinate of the player.
        player_y (int): The y-coordinate of the player.
        bullet_width (int): The width of the bullet.
        bullet_height (int): The height of the bullet.

    Returns:
        pygame.Rect: A new bullet rectangle.
    """
    bullet_x = player_x + player_width // 2 - bullet_width // 2  # Calculate the bullet's x-coordinate
    bullet_y = player_y - bullet_height                         # Calculate the bullet's y-coordinate
    bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
    return bullet_rect

def move_bullets(bullet_list):
    """
    Move the bullets and remove any bullets that go off-screen.

    Args:
        bullet_list (list): A list of bullet rectangles.

    Returns:
        list: The updated list of bullet rectangles.
    """
    new_bullet_list = []
    for bullet_rect in bullet_list:
        bullet_rect.y -= 10                  # Move the bullet upwards
        if bullet_rect.y >= 0:               # If the bullet is still on-screen
            new_bullet_list.append(bullet_rect)
    return new_bullet_list

def check_collisions(enemy_list, bullet_list):
    """
    Check for collisions between bullets and enemies, and remove any collided objects.

    Args:
        enemy_list (list): A list of enemy rectangles.
        bullet_list (list): A list of bullet rectangles.

    Returns:
        list: The updated list of enemy rectangles.
    """
    new_enemy_list = enemy_list[:]                          # Create a copy of the enemy list
    for enemy_rect in enemy_list:
        for bullet_rect in bullet_list:
            if enemy_rect.colliderect(bullet_rect):         # If a bullet hits an enemy
                new_enemy_list.remove(enemy_rect)           # Remove the enemy from the list
                bullet_list.remove(bullet_rect)             # Remove the bullet from the list
                break
    return new_enemy_list

def draw_objects(screen, player_rect, enemy_list, bullet_list):
    """
    Draw the player, enemies, and bullets on the screen.

    Args:
        screen (pygame.Surface): The game window surface.
        player_rect (pygame.Rect): The player rectangle.
        enemy_list (list): A list of enemy rectangles.
        bullet_list (list): A list of bullet rectangles.
    """
    screen.fill(BLACK)                                      # Fill the screen with black
    pygame.draw.rect(screen, GREEN, player_rect)            # Draw the player
    for enemy_rect in enemy_list:                           # Draw the enemies
        pygame.draw.rect(screen, WHITE, enemy_rect)
    for bullet_rect in bullet_list:                         # Draw the bullets
        pygame.draw.rect(screen, WHITE, bullet_rect)