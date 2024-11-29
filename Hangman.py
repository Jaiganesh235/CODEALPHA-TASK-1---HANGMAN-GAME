import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.word_list = ["data","scientists","fullstack","machine","learning","python", "hangman", "challenge", "experience", "career", "showcase", "programming","Java","codealpha","internship","analytics"]
        self.previous_word = None
        self.word = self.select_new_word()
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = 0
        self.max_attempts = 6
        self.guessed_letters = set()
        
        # Setup UI elements
        self.setup_ui()
        
    def setup_ui(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 24, "bold"), fg="darkblue")
        self.title_label.pack(pady=10)
        
        # Canvas for hangman graphic
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="lightblue")
        self.canvas.pack(pady=20)
        
        # Label for word display
        self.word_label = tk.Label(self.root, text=" ".join(self.guessed_word), font=("Helvetica", 18), fg="black")
        self.word_label.pack(pady=10)
        
        # Label for guessed letters
        self.guessed_label = tk.Label(self.root, text="Guessed Letters: None", font=("Helvetica", 12), fg="gray")
        self.guessed_label.pack(pady=5)
        
        # Entry for player input
        self.entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_guess)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Guess a letter!", font=("Helvetica", 12), fg="darkblue")
        self.status_label.pack(pady=5)
        
        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game, font=("Helvetica", 12), bg="lightgreen")
        self.reset_button.pack(pady=10)

        # Initial hangman structure (gallows)
        self.draw_gallows()
    
    def select_new_word(self):
        # Ensure a new word is selected after reset
        word = random.choice(self.word_list)
        while word == self.previous_word:
            word = random.choice(self.word_list)
        self.previous_word = word
        return word
    
    def draw_gallows(self):
        # Draw the gallows structure on the canvas
        self.canvas.create_line(50, 250, 200, 250, width=5)  # Base
        self.canvas.create_line(125, 250, 125, 50, width=5)  # Vertical pole
        self.canvas.create_line(125, 50, 200, 50, width=5)   # Horizontal pole
        self.canvas.create_line(200, 50, 200, 80, width=3)   # Rope

    def update_hangman(self):
        # Draw each stage of the hangman based on the number of incorrect attempts
        if self.attempts == 1:
            self.canvas.create_oval(180, 80, 220, 120, width=2)  # Head
        elif self.attempts == 2:
            self.canvas.create_line(200, 120, 200, 180, width=2)  # Body
        elif self.attempts == 3:
            self.canvas.create_line(200, 130, 180, 160, width=2)  # Left Arm
        elif self.attempts == 4:
            self.canvas.create_line(200, 130, 220, 160, width=2)  # Right Arm
        elif self.attempts == 5:
            self.canvas.create_line(200, 180, 180, 220, width=2)  # Left Leg
        elif self.attempts == 6:
            self.canvas.create_line(200, 180, 220, 220, width=2)  # Right Leg

    def check_guess(self, event=None):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)  # Clear entry box
        
        if len(guess) != 1 or not guess.isalpha():
            self.status_label.config(text="Please enter a single alphabet.", fg="orange")
            return
        
        if guess in self.guessed_letters:
            self.status_label.config(text=f"You've already guessed '{guess}'. Try again.", fg="purple")
            return
        
        self.guessed_letters.add(guess)
        self.guessed_label.config(text="Guessed Letters: " + ", ".join(sorted(self.guessed_letters)))
        
        if guess in self.word:
            self.status_label.config(text=f"Good job! '{guess}' is in the word.", fg="green")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
            self.word_label.config(text=" ".join(self.guessed_word))
            
            # Check if the player has won
            if "_" not in self.guessed_word:
                self.status_label.config(text="Congratulations! You've won!", fg="blue")
                self.entry.config(state="disabled")
                return
        else:
            self.attempts += 1
            self.status_label.config(text=f"Sorry, '{guess}' is not in the word.", fg="red")
            self.update_hangman()
            
            # Check if the player has lost
            if self.attempts >= self.max_attempts:
                self.status_label.config(text=f"Game Over! The word was: {self.word}", fg="red")
                self.entry.config(state="disabled")
    
    def reset_game(self):
        # Reset game variables and UI elements
        self.word = self.select_new_word()
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = 0
        self.guessed_letters.clear()
        
        self.word_label.config(text=" ".join(self.guessed_word))
        self.guessed_label.config(text="Guessed Letters: None")
        self.status_label.config(text="Guess a letter!", fg="darkblue")
        self.entry.config(state="normal")
        self.canvas.delete("all")
        self.draw_gallows()  # Redraw the gallows structure

# Run the game
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
