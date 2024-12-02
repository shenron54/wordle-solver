# Wordle Solver

This repository contains a Python solution to automatically solve the popular 5-letter word guessing game **Wordle**. The program interacts with the [Wordle API](https://wordle.votee.dev:8000/redoc) to play the game and guess the correct word based on feedback received after each attempt. This project was developed as part of a coding interview for Votee HK.

---

## Problem Scenario

The task was to connect to an API that plays a Wordle-like puzzle and write a program that automatically guesses random words while adhering to the rules of Wordle. The API supports two game modes: 

1. **Daily Challenge:** The puzzle is fixed and changes daily.
2. **Random Challenge:** A random seed determines the target word.

The solution leverages Python to make strategic guesses and refine the word list based on feedback from the API.

---
## Notes to Assessors:
* I have included an ipython notebook called "solution.ipynb" which outlines my thought process while designing the solution and how I solved problems that I ran into. Please do check the same for more reference information 

## Features

- **Dual Modes:** Supports both "daily" and "random" game modes.
- **Dynamic Filtering:** Removes invalid words from the dataset based on API feedback.
- **Efficient Word Selection:** Chooses a random word from the remaining valid words to guess.
- **Custom Word Dataset:** Uses a CSV file of valid 5-letter words as the word bank.

---

## Requirements

### Software
- Python 3.7 or higher
- An active internet connection to interact with the Wordle API

### Python Libraries
- `requests` (for API calls)
- `random` (for random seed generation and word selection)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/wordle-solver.git
   cd wordle-solver
2. Install required dependencies:
    pip install requests
3. Place your dataset file containing valid 5-letter words in the repository directory. Ensure the file is named valid_solutions.csv or update the file path in the code.

# Usage
1. Open the main.py file and set the game mode:
    mode = 'random'  # Choose between 'random' or 'daily'
    * random: A randomly selected puzzle based on a generated seed.
    * daily: The fixed daily puzzle provided by the Wordle API.
2. Run the script:
    python main.py
3. Observe the output:
    * The program will print each attempt, including the guessed word and feedback from the API.
    * If successful, it will display the solved word. If not, it will stop after six attempts.