# CODEALPHA-TASK-1---HANGMAN-GAME

#### Overview
The Hangman game is a classic word-guessing game where players attempt to uncover a hidden word one letter at a time. This project is implemented in Python and uses a text-based interface. It is designed to be beginner-friendly, making it an excellent example of combining logic, loops, and conditional statements in Python.



#### Features  
1. Random Word Selection: The program selects a random word from a predefined list, ensuring unique gameplay each time.  
2. Letter Guessing: Players guess letters, and the program checks if the letter is part of the word.  
3. Feedback System: The program provides immediate feedback, showing correctly guessed letters and the current state of the word.  
4. Incorrect Guesses Tracking: The game allows a limited number of incorrect guesses, displayed to the player.  
5. Win or Lose Conditions: Players win by guessing all the letters correctly or lose if they exceed the maximum number of incorrect guesses.  



#### How It Works
1. The program initializes by selecting a random word and displaying underscores (_) representing each letter.  
2. Players input one letter at a time.  
3. If the guessed letter is correct, it is revealed in the word. Otherwise, it counts as an incorrect guess.  
4. The game continues until the player either:
   - Guesses all the letters correctly (Win).  
   - Exceeds the allowed incorrect guesses (Lose).  



#### Educational Benefits
This project helps learners:  
- Understand Python basics like loops, conditionals, and string manipulation.  
- Practice input/output operations in Python.  
- Learn how to structure a simple game with logic and feedback loops.  
- Get introduced to game design principles like state tracking and user interaction.



#### Future Enhancements
- Add a graphical user interface (GUI) for a more interactive experience.  
- Include different difficulty levels with varying word lengths and guess limits.  
- Provide a feature to load words dynamically from an external file or API.  



#### How to Run the Program
1. Clone or download this repository.  
2. Ensure Python is installed on your system.  
3. Run the `Hangman.py` file using the command:  
   ```bash
   python Hangman.py
   ```  



