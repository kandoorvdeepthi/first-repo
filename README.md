Dice Roller
This is a simple Python script that simulates rolling a pair of six-sided dice. It provides a quick way to generate random outcomes for games or simulations.

Features
1. Interactive Gameplay: Prompt-based interface that allows you to continue rolling or exit at any time.
2. Dual Dice Output: Generates two random integers between 1 and 6, formatted as a coordinate pair.
3. Input Validation: Includes basic error handling for inputs other than 'y' or 'n'.

How to Run
1. Ensure you have Python installed on your system.
2. Save the code as dice.py.
3. Open your terminal or command prompt.
4. Navigate to the directory containing the file and run:
Bash = "python dice.py"

Usage
1. Enter 'y' to roll the dice.
2. Enter 'n' to stop the program and exit.

Code Logic
The script utilizes Python's built-in random module to ensure unpredictable results for each roll. It uses a while True loop to maintain an active session until the user explicitly chooses to quit.
