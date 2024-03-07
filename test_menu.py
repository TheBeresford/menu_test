import pygame
import sys

# Initialise pygame
pygame.init()

# Set up the display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Menu")

# Load the texture image
DARK_TURQUOISE = (0, 153, 153)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create font
font = pygame.font.Font(None, 36)

# Button class
class Button:
    def __init__(self, text, x, y, width, height, radius = 10):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.radius = radius
        self.activate = False

    def draw(self):
        if self.active:
            highlight_rect = self.rect.copy()
            highlight_rect.inflate_ip(10, 10) # This increases the size of the highlight
            pygame.draw.rect(screen, (255, 255, 255, 100), highlight_rect, border_radius=self.radius)

        # Draw the button with rounded corners
        button_color = DARK_TURQUOISE if not self.active else WHITE
        pygame.draw.rect(screen, button_color, self.rect, border_radius=self.radius -3)
        pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=self.radius -3)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

# Create buttons
start_button = Button("Start", (SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 200) // 2, 200, 50)
settings_button = Button("Settings", (SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 200) // 2 + 70, 200, 50)
quit_button = Button("Quit", (SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 200) // 2 + 140, 200, 50)


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

    ## Fill the screen
    screen.fill(DARK_TURQUOISE)

    # Draw the buttons
    start_button.draw()
    settings_button.draw()
    quit_button.draw()

    pygame.display.flip()
