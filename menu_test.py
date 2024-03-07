import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Menu")

# Load the texture image
#menu_texture = pygame.image.load("menu_texture.png").convert_alpha()

# Colours
dark_turqouise = (0, 153, 153)
white = (255, 255, 255)
black = (0, 0, 0)

# Create a font
font = pygame.font.Font(None, 36)

# Button class
class Button:
    def __init__(self, text, x, y, width, height, radius=10):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.radius = radius
        self.active = False

    def draw(self):
        # Draw highlighted background if the button is active
        if self.active:
            highlight_rect = self.rect.copy()
            highlight_rect.inflate_ip(10, 10)  # Increase the size of the highlight
            pygame.draw.rect(screen, (255, 255, 255, 100), highlight_rect, border_radius=self.radius)

        # Draw the button with rounded corners
        button_color = dark_turquoise if self.active else white
        pygame.draw.rect(screen, button_color, self.rect, border_radius=self.radius)

        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=self.radius)
        text_surface = font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

# Create buttons
start_button = Button("Start", (screen_width - 200) // 2, (screen_height - 200) // 2, 200, 50)
settings_button = Button("Settings", (screen_width - 200) // 2, (screen_height - 200) // 2 + 70, 200, 50)
quit_button = Button("Quit", (screen_width - 200) // 2, (screen_height - 200) // 2 + 140, 200, 50)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for mouse hover over buttons
    mouse_pos = pygame.mouse.get_pos()
    start_button.active = start_button.rect.collidepoint(mouse_pos)
    settings_button.active = settings_button.rect.collidepoint(mouse_pos)
    quit_button.active = quit_button.rect.collidepoint(mouse_pos)

    # Fill the screen with the menu texture
    screen.fill(dark_turquoise)

    # Draw buttons with rounded corners
    start_button.draw()
    settings_button.draw()
    quit_button.draw()

    pygame.display.flip()
