# Software Engineering Lab Portfolio: Vibe Coding & MLOps (DVC & MLflow)

Welcome to the comprehensive repository containing two major modules:
1. **Vibe Coding Lab:** An AI-assisted / pair-programmed Tic-Tac-Toe development project with rigorous before-and-after implementation analysis.
2. **DVC & MLflow MLOps Lab:** Practical implementations of Data Version Control (DVC) and MLflow experiment tracking, both separately and fully integrated.

---

## 📁 Repository Structure

```text
.
├── VIBE_CODING/
│   ├── BEFORE CHANGES/         # Original Tic-Tac-Toe codebase with intentional bugs and pending tasks
│   └── AFTER CHANGES/          # Completed, fully functional game with advanced features & documentation
└── DVC AND ML FLOW/
    ├── dvc_data_versioning/    # Data Version Control (DVC) setup and demo checkout scripts
    ├── mlflow_experiment_tracking/ # MLflow model training and experiment tracking app
    └── dvc_mlflow_integrated/  # Integrated DVC + MLflow MLOps pipeline with model artifacts & UI
```

---

## 🕹️ Module 1: Vibe Coding - Tic-Tac-Toe Lab

This module demonstrates AI-assisted software engineering (vibe coding / LLM pair programming) to fix bugs and implement advanced features in a Pygame Tic-Tac-Toe application.

### Key Components:
* **`BEFORE CHANGES/`**: The starting state provided for the lab featuring single-player gameplay against a random computer opponent (`O`), along with deliberate bugs (missing diagonal wins, win/draw priority issues, post-game click acceptance, and lack of move validation).
* **`AFTER CHANGES/`**: The complete production-ready version featuring:
  - **Task 1 (Bug Fixes):** Full 8-line win detection (rows, columns, and **both diagonals**), correct win/draw priority on the final cell, and post-game click blocking.
  - **Task 2 (Scoreboard):** Persistent score tracking (X wins, O wins, draws) surviving round restarts (`R` key) and clearing only on match resets (`M` key).
  - **Task 3 (Move Validation):** Rejection of clicks on already-occupied cells.
  - **Task 4 (First-Player Choice & Restarts):** Toggle starting player (`C` key) between human (`X`) and computer (`O`), with automated computer opening moves and separate round vs. match controls.
  - **Documentation:** Complete change logs, plans, and testing guides (`COMBINED_DOCUMENTATION.md`, `CHANGELOG.md`, `PLAN.md`, etc.).

### Getting Started (Tic-Tac-Toe):
```bash
cd VIBE_CODING/"AFTER CHANGES"/tic-tac-toe
pip install -r requirements.txt
python main.py
```

**Controls:**
* **Mouse Click:** Place symbol on empty cell
* **`R` Key:** Restart round (preserves scoreboard)
* **`M` Key:** Reset match (clears scoreboard)
* **`C` Key:** Change starting player (`X` or `O`)

---

## 📊 Module 2: DVC & MLflow (MLOps Pipeline)

This module explores foundational and advanced MLOps practices using Data Version Control and MLflow.

### Submodules:
1. **`dvc_data_versioning/`**: Demonstrates data version tracking using DVC (`data.csv`, `.dvc` tracking files, and `demo_checkout.py` for version checkout workflows).
2. **`mlflow_experiment_tracking/`**: Implements experiment tracking, metric logging, and artifact management using MLflow (`train_mlflow.py` and Flask web app `app.py`).
3. **`dvc_mlflow_integrated/`**: Combines DVC data pipelines with MLflow experiment tracking (`train_integrated.py`, logged models in `mlruns/`, SQLite tracking backend `mlflow.db`, and inference web app).

---

## 🚀 Getting Started & Setup

To clone and run this repository:

```bash
git clone <repository-url>
cd GITHUB
```
