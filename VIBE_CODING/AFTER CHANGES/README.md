# Tic-Tac-Toe Lab - COMPLETED VERSION

This is the completed version of the Tic-Tac-Toe lab with all bugs fixed and features implemented.

---

## What's Included

A fully functional Tic-Tac-Toe game with:

- A 3x3 board you click on to place X
- You always play X; the computer automatically plays O right after you
- **Complete win and draw detection** including diagonals
- **Persistent scoreboard** tracking X wins, O wins, and draws
- **Move validation** preventing invalid moves
- **First-player choice** - choose whether X or O starts
- **Separate restart controls** for round vs match reset

---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the game:

```bash
python main.py
```

---

## Controls

### Game Controls:
- **Mouse Click**: Click a cell to place your symbol (X)
- **R Key**: Restart round (keeps scoreboard and settings)
- **M Key**: Reset match (clears scoreboard and resets everything)
- **C Key**: Change first player (toggle between X starts / O starts)

### How to Play:
1. Click an empty cell to place X
2. Computer automatically places O
3. First to get 3 in a row (horizontal, vertical, or diagonal) wins
4. Scoreboard tracks wins across multiple rounds

---

## Features Implemented

### ✅ Task 1: Win and Draw Detection (FIXED)
**All three issues resolved:**

1. **Diagonal wins now detected** 
   - Both diagonal directions properly recognized
   - Top-left to bottom-right
   - Top-right to bottom-left

2. **Win priority fixed**
   - Winning moves always show wins (never incorrectly shows "Draw!")
   - Even when winning move fills the last cell

3. **Post-game moves blocked**
   - No moves accepted after round ends
   - Must press R or M to continue

**Technical Details:**
- Updated `rules.py` to include diagonal checks
- Fixed `check_round_end()` logic order in `game_engine.py`

---

### ✅ Task 2: Persistent Scoreboard (IMPLEMENTED)
**Features:**
- Tracks X wins, O wins, and draws
- Displays at top of screen at all times
- Persists across round restarts (R key)
- Only clears on match reset (M key)

**Display Format:**
```
SCORE - X: 3  |  O: 1  |  Draws: 2
```

**Technical Details:**
- Added `x_wins`, `o_wins`, `draws` attributes to `GameEngine`
- Created `draw_scoreboard()` function in `renderer.py`
- Scores update automatically when rounds end

---

### ✅ Task 3: Move Validation (IMPLEMENTED)
**Features:**
- Clicking occupied cells is rejected
- No overwrites of existing symbols
- Turn and board state remain unchanged on invalid moves

**Technical Details:**
- Added occupied cell check in `handle_click()` method
- Returns early if cell already contains X or O

---

### ✅ Task 4: First-Player Choice & Restart Controls (IMPLEMENTED)

**First-Player Choice:**
- Press C key to toggle who starts first
- Default: X starts first
- When O starts: computer automatically makes first move
- Choice persists across round restarts
- Indicator shows "First: X" or "First: O" on screen

**Separate Restart Controls:**

1. **R Key - Restart Round:**
   - Clears the board
   - Keeps the scoreboard
   - Keeps first-player choice
   - Perfect for playing another round

2. **M Key - Reset Match:**
   - Clears the board
   - Resets scoreboard to 0-0-0
   - Resets first-player to X
   - Starts completely fresh

**Technical Details:**
- Added `first_player` attribute to track starting player
- Modified `__init__()` to accept `preserve_scores` and `preserve_first_player` parameters
- Added C, M key handlers to `handle_keydown()`
- Computer takes first move automatically when O starts

---

## Expected Behavior

### Win Detection:
- ✅ All 8 winning lines detected (3 rows + 3 columns + 2 diagonals)
- ✅ Winning move on last cell correctly shows win
- ✅ Draw only occurs when board full with no winner

### Move Validation:
- ✅ Occupied cells cannot be clicked
- ✅ No moves accepted after round ends
- ✅ Only human player can click during their turn

### Scoreboard:
- ✅ Persists across round restarts (R key)
- ✅ Clears on match reset (M key)
- ✅ Updates automatically after each round

### First-Player Choice:
- ✅ Toggle with C key
- ✅ Computer moves first when O is selected
- ✅ Choice persists across rounds

---

## Folder Structure

```
tic-tac-toe/
├── main.py              # Entry point - Pygame main loop
├── requirements.txt     # Python dependencies
└── game/                # Game logic modules
    ├── __init__.py      # Python package
    ├── game_engine.py   # Main game state and controller (MODIFIED)
    ├── rules.py         # Win/draw detection logic (MODIFIED)
    ├── ai.py            # Computer opponent logic
    └── renderer.py      # Pygame drawing functions (MODIFIED)
```

---

## Implementation Summary

### Files Modified:
1. **game_engine.py** - Major updates:
   - Scoreboard tracking (x_wins, o_wins, draws)
   - First-player choice system
   - Separate restart controls (R, M, C keys)
   - Bug fixes (win priority, move blocking, validation)

2. **rules.py** - Additions:
   - Diagonal win detection (2 new checks)

3. **renderer.py** - Additions:
   - `draw_scoreboard()` function
   - Scoreboard display formatting

### Code Quality:
- Clear comments explaining all changes
- Maintains original code structure
- No breaking changes to existing functionality
- Easy to understand and maintain

---

## Testing Checklist

- [x] Diagonal wins (both directions)
- [x] Winning move on last cell shows win
- [x] Post-game clicks blocked
- [x] Occupied cell clicks rejected
- [x] Scoreboard persists on round restart (R)
- [x] Scoreboard clears on match reset (M)
- [x] First-player toggle works (C key)
- [x] Computer moves first when O selected
- [x] All row and column wins detected
- [x] Genuine draws detected correctly

---

## Development Notes

**Phase 2 (Bug Fixes):**
- Fixed diagonal win detection
- Fixed win/draw priority logic
- Added post-game move blocking
- Added move validation

**Phase 3 (Features):**
- Implemented persistent scoreboard
- Added first-player choice system
- Separated restart controls
- Enhanced UI with score display

---

## Credits

**Lab Assignment:** Tic-Tac-Toe Lab
**Completed Using:** AI-assisted development (LLM pair programming)
**Technologies:** Python 3.10+, Pygame

---