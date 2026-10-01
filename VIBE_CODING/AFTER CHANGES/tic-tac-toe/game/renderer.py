"""
renderer: all pygame drawing lives here, kept separate from game logic.

ADDED (Phase 3): Scoreboard display function
FIXED: Increased window height for better UI display
"""

import pygame

WIDTH, HEIGHT = 400, 580  # Increased height from 500 to 580 for better spacing
BOARD_SIZE = 360
CELL_SIZE = BOARD_SIZE // 3
BOARD_TOP = 100
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (245, 245, 245)
COLOR_LINE = (60, 60, 60)
COLOR_X = (200, 60, 60)
COLOR_O = (60, 100, 200)
COLOR_TEXT = (30, 30, 30)
COLOR_SCOREBOARD = (50, 50, 150)


def board_pos_to_cell(pos):
    x, y = pos
    y -= BOARD_TOP
    if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
        return None
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return int(row), int(col)


def draw_board(surface, board):
    surface.fill(COLOR_BG)
    for i in range(1, 3):
        pygame.draw.line(surface, COLOR_LINE, (i * CELL_SIZE, BOARD_TOP), (i * CELL_SIZE, BOARD_TOP + BOARD_SIZE), 3)
        pygame.draw.line(surface, COLOR_LINE, (0, BOARD_TOP + i * CELL_SIZE), (BOARD_SIZE, BOARD_TOP + i * CELL_SIZE), 3)

    for r in range(3):
        for c in range(3):
            symbol = board[r][c]
            if symbol is None:
                continue
            center = (c * CELL_SIZE + CELL_SIZE // 2, BOARD_TOP + r * CELL_SIZE + CELL_SIZE // 2)
            if symbol == 'X':
                offset = CELL_SIZE // 3
                pygame.draw.line(surface, COLOR_X, (center[0]-offset, center[1]-offset), (center[0]+offset, center[1]+offset), 6)
                pygame.draw.line(surface, COLOR_X, (center[0]+offset, center[1]-offset), (center[0]-offset, center[1]+offset), 6)
            else:
                pygame.draw.circle(surface, COLOR_O, center, CELL_SIZE // 3, 6)


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)


def draw_banner(surface, font, text):
    """
    Draw end-game banner with text wrapped across multiple lines if needed.
    """
    # Use a smaller font for the banner to fit everything
    small_font = pygame.font.SysFont("consolas", 16)
    
    # Split the message into two lines for better fit
    if " R=" in text:  # End game message with controls
        parts = text.split(" R=")
        line1 = parts[0]  # Winner or Draw message
        line2 = "R=Restart | M=Reset | C=Change"
        
        # Draw first line (winner/draw)
        surf1 = font.render(line1, True, (180, 40, 40))
        rect1 = surf1.get_rect(center=(surface.get_width() // 2, BOARD_TOP + BOARD_SIZE + 30))
        surface.blit(surf1, rect1)
        
        # Draw second line (controls)
        surf2 = small_font.render(line2, True, (60, 60, 60))
        rect2 = surf2.get_rect(center=(surface.get_width() // 2, BOARD_TOP + BOARD_SIZE + 60))
        surface.blit(surf2, rect2)
    else:
        # Regular banner
        surf = font.render(text, True, (180, 40, 40))
        rect = surf.get_rect(center=(surface.get_width() // 2, BOARD_TOP + BOARD_SIZE + 40))
        surface.blit(surf, rect)


def draw_scoreboard(surface, font, x_wins, o_wins, draws):
    """
    Draw the persistent scoreboard at the top of the screen.
    
    Args:
        surface: Pygame surface to draw on
        font: Font to use for text
        x_wins: Number of rounds X has won
        o_wins: Number of rounds O has won
        draws: Number of rounds that ended in a draw
    """
    # Create scoreboard text
    scoreboard_text = f"SCORE - X: {x_wins}  |  O: {o_wins}  |  Draws: {draws}"
    
    # Draw scoreboard centered at the top
    text_surface = font.render(scoreboard_text, True, COLOR_SCOREBOARD)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 20))
    surface.blit(text_surface, text_rect)
    
    # Draw a separator line below scoreboard
    pygame.draw.line(surface, COLOR_LINE, (10, 45), (WIDTH - 10, 45), 2)

