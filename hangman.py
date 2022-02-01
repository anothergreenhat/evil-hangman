# Joseph Madera

class Hangman:

    def __init__(self):
        self.full_dict = []
        self.current_dict = []
        self.word_length = 0
        self.guesses_left = 0
        self.guessed_chars = []
        self.show_remaining_words = False
        with open("dictionary.txt", "r") as dict_file:
            for word in dict_file:
                self.full_dict.append(word.rstrip())

    def __str__(self):
        pass

    def get_word_length_from_input(self):
        self.word_length = input("Enter the length of the word you wish to guess: ")
        while not isinstance(self.word_length, int):
            try:
                self.word_length = int(self.word_length)
            except ValueError:
                print("You must enter a number.")
                self.word_length = input("Enter the length of the word you wish to guess: ")

    def get_guess_number_from_input(self):
        self.guesses_left = input("Enter the amount of guesses you will have: ")
        while not isinstance(self.word_length, int):
            try:
                self.guesses_left = int(self.guesses_left)
            except ValueError:
                print("You must enter a number.")
                self.word_length = input("Enter the amount of guesses you will have: ")

    def get_remaining_words_yes_no_from_input(self):
        y = input("Would you like to display the list of remaining words after each guess? (yes or no): ")
        if y == "yes":
            self.show_remaining_words = True
        else:
            self.show_remaining_words = False
            print("I will not show you the remaining words.")

    def update_underscores(self):
        for i in range(self.word_length):
            print("_", end="")
        print()
        # TODO: process updates for underscoring

    def display_remaining_words(self):
        self.current_dict = [word for word in self.full_dict if len(word) == self.word_length]
        print(self.current_dict)

    def display_guessed_bad_chars(self):
        print("Guessed letters:", self.guessed_chars)

    def guess(self):
        guess_char = input("Enter a guess character: ")
        while not isinstance(guess_char, int):
            try:
                int(guess_char)
                print("You must enter a character.")
            except ValueError:
                print(guess_char)
                break
            guess_char = input("Enter a guess character: ")
        # TODO implement global word
        if guess_char in self.global_word:
            self.guesses_left -= 1
            self.guessed_chars.append(guess_char)
        else:
            pass


    def play(self):
        word_not_guessed = True
        self.get_word_length_from_input()
        self.get_guess_number_from_input()
        self.get_remaining_words_yes_no_from_input()
        while word_not_guessed:
            self.update_underscores()
            self.display_guessed_bad_chars()
            if self.show_remaining_words:
                self.display_remaining_words()
            self.guess()


