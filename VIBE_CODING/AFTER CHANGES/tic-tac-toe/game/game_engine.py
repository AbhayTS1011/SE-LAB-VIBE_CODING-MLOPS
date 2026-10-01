"""
GameEngine: owns the board, turn state, and round-end logic.

You (the player) always play X and click to move. The computer always
plays O and moves automatically right after you, using a simple
random-move AI (see game/ai.py) - this is given infrastructure, not
something you need to build.

FIXED (Phase 2): 
- Win/draw detection now checks for winner FIRST before checking for draw
- Move validation prevents clicking occupied cells
- Post-game moves are blocked

ADDED (Phase 3):
- Persistent scoreboard tracking X wins, O wins, and draws
- First-player choice (X or O can start)
- Separate restart controls:
  * R key: Restart round (keep scores)
  * M key: Reset match (clear scores)
  * C key: Change who starts first
"""

from game.rules import check_winner, is_board_full
from game.renderer import board_pos_to_cell
from game.ai import choose_move

HUMAN_SYMBOL = 'X'
COMPUTER_SYMBOL = 'O'


class GameEngine:
    def __init__(self, preserve_scores=False, preserve_first_player=False):
        """
        Initialize or reset the game engine.
        
        Args:
            preserve_scores: If True, keep scoreboard values (for round restart)
            preserve_first_player: If True, keep first player choice
        """
        # Preserve scoreboard if requested (for round restart)
        if preserve_scores and hasattr(self, 'x_wins'):
            x_wins = self.x_wins
            o_wins = self.o_wins
            draws = self.draws
            first_player = self.first_player if preserve_first_player else self.first_player
        else:
            x_wins = 0
            o_wins = 0
            draws = 0
            first_player = 'X' if not hasattr(self, 'first_player') else self.first_player
        
        # Game state
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = first_player  # Start with chosen first player
        self.round_over = False
        self.winner = None   # 'X', 'O', or None (meaning draw, only valid when round_over)
        
        # Scoreboard (persistent across rounds)
        self.x_wins = x_wins
        self.o_wins = o_wins
        self.draws = draws
        
        # First player choice
        self.first_player = first_player
        
        # If O starts first, computer should take first move
        if self.first_player == COMPUTER_SYMBOL:
            self._maybe_take_computer_turn()

    def handle_click(self, pos):
        # FIXED: Block moves after round is over
        if self.round_over:
            return
            
        if self.current_player != HUMAN_SYMBOL:
            return   # not your turn - the computer is about to move (or already has)
        
        cell = board_pos_to_cell(pos)
        if cell is None:
            return
        
        row, col = cell
        
        # FIXED: Check if cell is already occupied (TASK 3 fix)
        if self.board[row][col] is not None:
            return  # Cell is occupied, reject the move
        
        self.board[row][col] = self.current_player
        self.check_round_end()
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self._maybe_take_computer_turn()

    def _maybe_take_computer_turn(self):
        if self.round_over or self.current_player != COMPUTER_SYMBOL:
            return
        move = choose_move(self.board)
        if move is None:
            return
        row, col = move
        self.board[row][col] = self.current_player
        self.check_round_end()
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def handle_keydown(self, key):
        import pygame
        
        # R key: Restart round (preserve scores and first player)
        if key == pygame.K_r:
            self.__init__(preserve_scores=True, preserve_first_player=True)
        
        # M key: Reset match (clear everything)
        elif key == pygame.K_m:
            self.__init__(preserve_scores=False, preserve_first_player=False)
        
        # C key: Change first player (toggle between X and O)
        elif key == pygame.K_c:
            self.first_player = 'O' if self.first_player == 'X' else 'X'
            self.__init__(preserve_scores=True, preserve_first_player=True)

    def check_round_end(self):
        # FIXED: Check for winner FIRST before checking for draw
        winner = check_winner(self.board)
        if winner:
            self.round_over = True
            self.winner = winner
            # Update scoreboard
            if winner == 'X':
                self.x_wins += 1
            else:
                self.o_wins += 1
            return
        
        # Only check for draw if there's no winner
        if is_board_full(self.board):
            self.round_over = True
            self.winner = None  # None means draw
            self.draws += 1  # Update draw count

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_board(surface, self.board)
        
        # Draw scoreboard at the top
        renderer.draw_scoreboard(surface, font, self.x_wins, self.o_wins, self.draws)
        
        # Draw turn indicator
        turn_label = "Your turn (X)" if self.current_player == HUMAN_SYMBOL else "Computer's turn (O)"
        renderer.draw_text(surface, font, turn_label, (10, 70))
        
        # Draw first player indicator
        first_player_text = f"First: {self.first_player}"
        renderer.draw_text(surface, font, first_player_text, (WIDTH - 100, 70))

        # Draw end-of-round message
        if self.round_over:
            text = f"{self.winner} wins!" if self.winner else "Draw!"
            renderer.draw_banner(surface, font, f"{text} R=New Round | M=Reset Match | C=Change First")

# Import WIDTH for first player display
from game.renderer import WIDTH
