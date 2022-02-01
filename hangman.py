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
        self.current_dict = [word for word in self.full_dict if len(word) == self.word_length]

    def get_guess_number_from_input(self):
        self.guesses_left = input("Enter the amount of guesses you will have: ")
        while not isinstance(self.guesses_left, int):
            try:
                self.guesses_left = int(self.guesses_left)
            except ValueError:
                print("You must enter a number.")
                self.guesses_left = input("Enter the amount of guesses you will have: ")

    def get_remaining_words_yes_no_from_input(self):
        yes_or_no = False
        while not yes_or_no:
            y = input("Would you like to display the list of remaining words after each guess? (yes or no): ")
            if y == "yes":
                self.show_remaining_words = True
                yes_or_no = True
            elif y == "no":
                self.show_remaining_words = False
                yes_or_no = True
            else:
                print("You must enter yes or no.")

    def update_underscores(self):
        for i in range(self.word_length):
            print("_", end="")
        print("   guesses remaining:", self.guesses_left)
        # TODO: process updates for underscoring

    def display_remaining_words(self):
        print(self.current_dict)

    def display_guessed_bad_chars(self):
        print("Guessed letters:", self.guessed_chars)

    def guess(self):
        guess_char = input("Enter a guess character: ")
        # TODO if guess is in set{guessed_letters} then retry
        while not isinstance(guess_char, int):
            try:
                int(guess_char)
                print("You must enter a character.")
            except ValueError:
                if len(guess_char) > 1:
                    print("You must enter a character.")
                    guess_char = input("Enter a guess character: ")
                    continue
                break
            guess_char = input("Enter a guess character: ")
        bad_guess = self.check_if_guess_is_bad(guess_char)
        if bad_guess:
            self.guesses_left -= 1
            self.guessed_chars.append(guess_char)
        else:
            pass
        self.update_underscores()
        self.display_guessed_bad_chars()

    def check_if_guess_is_bad(self, guess_char):
        list_with_guess = [word for word in self.current_dict if guess_char in word]
        list_without_guess = [word for word in self.current_dict if guess_char not in word]
        if len(list_without_guess) != 0:
            self.current_dict = list_without_guess
            return True
        else:
            # self.current_dict = largest word family with letter in it

            return False


    def play(self):
        word_not_guessed = True
        self.get_word_length_from_input()
        self.get_guess_number_from_input()
        self.get_remaining_words_yes_no_from_input()
        self.update_underscores()
        while self.guesses_left > 0:
            if self.show_remaining_words:
                self.display_remaining_words()
            self.guess()


