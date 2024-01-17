import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load the motif image
# Replace with the actual path of your motif image
motif_image = pygame.image.load("bgimage.png")
motif_image = pygame.transform.scale(motif_image, (WIDTH, HEIGHT))

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MOSAIC BROWSING")

# Function to draw text on the screen


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to create the initial window


def initial_window():
    # Large font for "MOSAIC BROWSING"
    font_large = pygame.font.Font(None, 100)
    font_small = pygame.font.Font(None, 30)  # Small font for buttons

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle button clicks for the initial window
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    second_window()
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Draw the motif image background
        screen.blit(motif_image, (0, 0))

        # Create and draw buttons for the initial window
        button_width, button_height = 150, 50
        start_button_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 4, HEIGHT // 2, button_width, button_height))
        exit_button_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 2, HEIGHT // 2, button_width, button_height))

        # Draw the message box for the initial window
        message_box_width, message_box_height = 800, 100
        message_box_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 2 - message_box_width // 2, HEIGHT // 4, message_box_width, message_box_height))

        # Draw the "MOSAIC BROWSING" text inside the message box
        draw_text("MOSAIC BROWSING", font_large, BLACK, WIDTH //
                  2, HEIGHT // 4 + message_box_height // 2)

        # Draw button text for the initial window
        draw_text("START", font_small, BLACK, WIDTH // 4 +
                  button_width // 2, HEIGHT // 2 + button_height // 2)
        draw_text("EXIT", font_small, BLACK, WIDTH // 2 +
                  button_width // 2, HEIGHT // 2 + button_height // 2)

        # Update the screen
        pygame.display.flip()

# Function to create the second window
# Function to create the second window


def second_window():
    font_large = pygame.font.Font(None, 60)  # Large font for headings
    # Small font for labels and buttons
    font_small = pygame.font.Font(None, 30)

    motif_rows_input = ""
    motif_cols_input = ""
    mosaic_rows_input = ""
    mosaic_cols_input = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle button clicks for the second window
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    initial_window()
                elif next_button_rect.collidepoint(pygame.mouse.get_pos()):
                    if motif_rows_input and motif_cols_input and mosaic_rows_input and mosaic_cols_input:
                        motif_rows = int(motif_rows_input)
                        motif_cols = int(motif_cols_input)
                        mosaic_rows = int(mosaic_rows_input)
                        mosaic_cols = int(mosaic_cols_input)
                        third_window(motif_rows, motif_cols,
                                     mosaic_rows, mosaic_cols)

            # Handle text input for motif and mosaic rows/columns
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    if motif_rows_input_rect.collidepoint(pygame.mouse.get_pos()):
                        motif_rows_input += event.unicode
                    elif motif_cols_input_rect.collidepoint(pygame.mouse.get_pos()):
                        motif_cols_input += event.unicode
                    elif mosaic_rows_input_rect.collidepoint(pygame.mouse.get_pos()):
                        mosaic_rows_input += event.unicode
                    elif mosaic_cols_input_rect.collidepoint(pygame.mouse.get_pos()):
                        mosaic_cols_input += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    if motif_rows_input_rect.collidepoint(pygame.mouse.get_pos()):
                        motif_rows_input = motif_rows_input[:-1]
                    elif motif_cols_input_rect.collidepoint(pygame.mouse.get_pos()):
                        motif_cols_input = motif_cols_input[:-1]
                    elif mosaic_rows_input_rect.collidepoint(pygame.mouse.get_pos()):
                        mosaic_rows_input = mosaic_rows_input[:-1]
                    elif mosaic_cols_input_rect.collidepoint(pygame.mouse.get_pos()):
                        mosaic_cols_input = mosaic_cols_input[:-1]

        # Draw the motif image background
        screen.blit(motif_image, (0, 0))

        # Draw input boxes for motif and mosaic rows/columns
        input_box_width, input_box_height = 100, 30
        motif_rows_input_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 3, HEIGHT // 4, input_box_width, input_box_height))
        motif_cols_input_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 3, HEIGHT // 3, input_box_width, input_box_height))
        mosaic_rows_input_rect = pygame.draw.rect(
            screen, WHITE, (2 * WIDTH // 3, HEIGHT // 4, input_box_width, input_box_height))
        mosaic_cols_input_rect = pygame.draw.rect(
            screen, WHITE, (2 * WIDTH // 3, HEIGHT // 3, input_box_width, input_box_height))

        # Draw labels for input boxes
        draw_text("Motif Rows:", font_small, BLACK, WIDTH // 3 -
                  input_box_width, HEIGHT // 4 + input_box_height // 2)
        draw_text("Motif Cols:", font_small, BLACK, WIDTH // 3 -
                  input_box_width, HEIGHT // 3 + input_box_height // 2)
        draw_text("Mosaic Rows:", font_small, BLACK, 2 * WIDTH // 3 -
                  input_box_width, HEIGHT // 4 + input_box_height // 2)
        draw_text("Mosaic Cols:", font_small, BLACK, 2 * WIDTH // 3 -
                  input_box_width, HEIGHT // 3 + input_box_height // 2)

        # Draw the input texts inside the input boxes
        draw_text(motif_rows_input, font_small, BLACK, WIDTH // 3 +
                  input_box_width // 2, HEIGHT // 4 + input_box_height // 2)
        draw_text(motif_cols_input, font_small, BLACK, WIDTH // 3 +
                  input_box_width // 2, HEIGHT // 3 + input_box_height // 2)
        draw_text(mosaic_rows_input, font_small, BLACK, 2 * WIDTH //
                  3 + input_box_width // 2, HEIGHT // 4 + input_box_height // 2)
        draw_text(mosaic_cols_input, font_small, BLACK, 2 * WIDTH //
                  3 + input_box_width // 2, HEIGHT // 3 + input_box_height // 2)

        # Create and draw back and next buttons
        button_width, button_height = 150, 50
        back_button_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 4, 2 * HEIGHT // 3, button_width, button_height))
        next_button_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 2, 2 * HEIGHT // 3, button_width, button_height))

        # Draw button text with the small font
        draw_text("BACK", font_small, BLACK, WIDTH // 4 +
                  button_width // 2, 2 * HEIGHT // 3 + button_height // 2)
        draw_text("NEXT", font_small, BLACK, WIDTH // 2 +
                  button_width // 2, 2 * HEIGHT // 3 + button_height // 2)

        # Update the screen
        pygame.display.flip()

# Function to create the third window


def third_window(motif_rows, motif_cols, mosaic_rows, mosaic_cols):
    font_large = pygame.font.Font(None, 60)  # Large font for headings
    # Small font for labels and buttons
    font_small = pygame.font.Font(None, 30)

    motif_tile_size = 50
    motif_grid_x, motif_grid_y = WIDTH // 4 - \
        motif_tile_size * 3, HEIGHT // 4 - motif_tile_size * 2
    motif_grid = [[0 for _ in range(motif_cols)] for _ in range(motif_rows)]
    motif_grid_rects = []

    mosaic_tile_size = 50
    mosaic_grid_x, mosaic_grid_y = 2 * WIDTH // 3 - mosaic_cols * \
        mosaic_tile_size + mosaic_tile_size * 3, HEIGHT // 4 - mosaic_tile_size * 2
    mosaic_grid = [[0 for _ in range(mosaic_cols)] for _ in range(mosaic_rows)]
    mosaic_grid_rects = []

    def draw_grid(grid_x, grid_y, rows, cols, tile_size, input_box):
        for i in range(rows + 1):
            pygame.draw.line(screen, BLACK, (grid_x, grid_y + i * tile_size),
                             (grid_x + cols * tile_size, grid_y + i * tile_size))
        for j in range(cols + 1):
            pygame.draw.line(screen, BLACK, (grid_x + j * tile_size, grid_y),
                             (grid_x + j * tile_size, grid_y + rows * tile_size))
        input_box.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    class InputBox:
        def _init_(self, x, y, width, height, font):
            self.rect = pygame.Rect(x, y, width, height)
            self.font = font
            self.text = ''
            self.active = False
            self.grid = None
            self.row = None
            self.col = None

        def handle_event(self, event):
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        self.grid[self.row][self.col] = int(self.text)
                    except ValueError:
                        pass
                    self.text = ''
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        def draw(self, screen):
            color = (255, 255, 255) if self.active else (200, 200, 200)
            pygame.draw.rect(screen, color, self.rect)
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    motif_input_box = InputBox(motif_grid_x, motif_grid_y, motif_cols *
                               motif_tile_size, motif_rows * motif_tile_size, pygame.font.Font(None, 36))
    mosaic_input_box = InputBox(mosaic_grid_x, mosaic_grid_y, mosaic_cols *
                                mosaic_tile_size, mosaic_rows * mosaic_tile_size, pygame.font.Font(None, 36))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle button clicks for the third window
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if clicked on the "BACK" button
                if back_button_rect.collidepoint(mouse_x, mouse_y):
                    second_window()
                # Check if clicked on the "NEXT" button
                elif next_button_rect.collidepoint(mouse_x, mouse_y):
                    fourth_window(motif_rows, motif_cols,
                                  mosaic_rows, mosaic_cols)

            # Handle text input events for input boxes
            motif_input_box.handle_event(event)
            mosaic_input_box.handle_event(event)

        # Draw the motif image background
        screen.blit(motif_image, (0, 0))

        # Create and draw back and next buttons, moved a little down
        button_width, button_height = 150, 50
        back_button_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 4, 2 * HEIGHT // 3 + button_height // 2, button_width, button_height))
        next_button_rect = pygame.draw.rect(
            screen, WHITE, (WIDTH // 2, 2 * HEIGHT // 3 + button_height // 2, button_width, button_height))

    # Draw button text with the small font, moved a little down
        draw_text("BACK", font_small, BLACK, WIDTH // 4 +
                  button_width // 2, 2 * HEIGHT // 3 + button_height)
        draw_text("NEXT", font_small, BLACK, WIDTH // 2 +
                  button_width // 2, 2 * HEIGHT // 3 + button_height)

        # Draw input boxes for motif and mosaic grids
        motif_input_box.draw(screen)
        mosaic_input_box.draw(screen)

        # Draw grids inside the input boxes
        draw_grid(motif_grid_x, motif_grid_y, motif_rows,
                  motif_cols, motif_tile_size, motif_input_box)
        draw_grid(mosaic_grid_x, mosaic_grid_y, mosaic_rows,
                  mosaic_cols, mosaic_tile_size, mosaic_input_box)

        # Update the screen
        pygame.display.flip()


if __name__ == "__main__":
    initial_window()
