class HintProvider:
    """
    A class to provide hints for word search
    """

    def __init__(self, words, grid, word_positions):
        """
        Initializes the HintProvider object.

        Args:
            words (list): A list of words in the word search.
            grid (list): The word search grid.
        """
        self.words = words
        self.grid = grid
        self.word_positions = word_positions
        self.hint_progress = {word: 0 for word in words}

    def provide_word_search_hint(self):
        """
        Highlights the first letter of one of the words in the grid by adding quotes.

        Returns:
            list: The updated grid with the first letter of a word highlighted.
        """
        for word in self.words:
            if self.hint_progress[word] < len(word): #Go until all letters are red
                x_pos, y_pos, dx, dy = self.word_positions[word]
                progress = self.hint_progress[word]
                
                #Get the next letter in the word
                new_x = x_pos + progress * dx
                new_y = y_pos + progress * dy
                self.grid[new_x][new_y] = f"\033[31m{word[progress]}\033[0m"  #Colors the letter red(https://stackoverflow.com/questions/72118363/how-do-i-color-a-string-in-python-terminal)

                self.hint_progress[word] += 1 #Count progress
                return word 
                
    def display_word_search_hints(self):
        """
        Displays the grid with the hint applied (quotes around the first letter).
        """
        print("\nHighlighted first letter of a word:")
        print(self.words) 
        for row in self.grid:
            print(" ".join(row))
            
    def ask_for_hint(self):
        """
        Keeps asking for hints until all words are fully highlighted.
        """
        while True:
            user_input = input("\nWould you like a hint? (Y/N): ").strip().upper()
            if user_input == "Y":
                word = self.provide_word_search_hint()  # Apply the next hint
                if word:
                    print(f"Hint: Revealing the next letter of the word '{word}'")
                    self.display_word_search_hints()
                else:
                    print("All words have been fully highlighted!")
                    break
            elif user_input == "N":
                print("Alright, no more hints will be provided. Good luck!")
                break
            else:
                print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
