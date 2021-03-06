# Joseph Madera

# I found this method to find the maximum length list from a dictionary and return its key
def find_longest_family_key(families):
    return max(families, key=lambda family_key: len(set(families[family_key])))


class Hangman:

    def __init__(self):
        self.full_dict = []
        self.current_dict = []
        self.word_length = 0
        self.guesses_left = 0
        self.bad_guessed_chars = []
        self.guess_key = ""
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
        print(self.guess_key)

    def display_guesses_remaining(self):
        print("Guesses remaining:", self.guesses_left)

    def display_remaining_words(self):
        print(self.current_dict)

    def display_guessed_bad_chars(self):
        print("Guessed letters:", self.bad_guessed_chars)

    def display_empty_starting_underscores(self):
        for i in range(self.word_length):
            print("_", end="")
        print()

    def get_guess_char_from_input(self):
        guess_char = input("Enter a guess character: ")
        while not isinstance(guess_char, int):
            try:
                int(guess_char)
                print("You must enter a character.")
            except ValueError:
                if guess_char in self.bad_guessed_chars or guess_char in self.guess_key:
                    print("Character has already been guessed.")
                    guess_char = input("Enter a guess character: ")
                    continue
                if len(guess_char) > 1:
                    print("You must enter a character.")
                    guess_char = input("Enter a guess character: ")
                    continue
                break
            guess_char = input("Enter a guess character: ")
        return guess_char

    def get_longest_family_key(self, guess_char):
        families = self.get_families(guess_char)
        longest_family_key = find_longest_family_key(families)
        self.current_dict = families[longest_family_key]
        return longest_family_key

    def get_families(self, guess_char):
        dict_key = ""
        families = {}
        for word in self.current_dict:
            for char in word:
                if char == guess_char:
                    dict_key += guess_char
                elif char in self.guess_key:
                    dict_key += char
                else:
                    dict_key += "_"
            if dict_key in families:
                families[dict_key].append(word)
            else:
                families[dict_key] = [word]
            dict_key = ""
        return families

    def guess(self):
        guess_char = self.get_guess_char_from_input()
        self.guess_key = self.get_longest_family_key(guess_char)
        if guess_char not in self.guess_key:
            self.guesses_left -= 1
            self.bad_guessed_chars.append(guess_char)
        self.update_underscores()
        self.display_guessed_bad_chars()
        if "_" not in self.guess_key:
            return True
        else:
            return False

    def guess_word(self):
        is_word_guessed = False
        while self.guesses_left > 0 and not is_word_guessed:
            self.display_guesses_remaining()
            if self.show_remaining_words:
                self.display_remaining_words()
            is_word_guessed = self.guess()
        return is_word_guessed

    def play(self):
        self.__init__()
        self.get_word_length_from_input()
        self.get_guess_number_from_input()
        self.get_remaining_words_yes_no_from_input()
        self.display_empty_starting_underscores()
        is_word_guessed = self.guess_word()
        if is_word_guessed:
            print("Congrats, you won! >:(")
        else:
            print("The word was '", self.current_dict[0], "'", sep="")
            print("I win, you lose! >:)")

