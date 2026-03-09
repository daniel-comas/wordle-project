import random
from termcolor import cprint

class WordList:
    def __init__(self, filename):
        self.words = self.load_words(filename)
    
    def load_words(self, filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    
    def pick_word(self):
        return random.choice(self.words)

def color_feedback(guess, target):
    feedback = []
    target_letters = list(target)
    
    for i, letter in enumerate(guess):
        if letter == target[i]:
            feedback.append((letter, 'green'))
            target_letters[i] = None
        elif letter in target_letters:
            feedback.append((letter, 'yellow'))
            target_letters[target_letters.index(letter)] = None
        else:
            feedback.append((letter, 'grey'))
    
    return feedback

def wordle_game():
    word_list = WordList("words.txt")
    target_word = word_list.pick_word()
    attempts = 6
    
    print("Welcome to Wordle! Guess the 5-letter word.")
    
    for _ in range(attempts):
        guess = input("Enter your 5-letter guess: ").strip().lower()
        
        if len(guess) != 5 or guess not in word_list.words:
            print("Invalid word. Try again.")
        
        feedback = color_feedback(guess, target_word)
        for letter, color in feedback:
            cprint(letter, color, end=' ')
        print()
        
        if guess == target_word:
            print("Congratulations! You guessed the word.")
            return
    
    print(f"Game over! The correct word was: {target_word}")

if __name__ == "__main__":
    wordle_game()
