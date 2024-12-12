class PuzzleSolver:
    """
    A class to solve puzzles like word search by highlighting all letters of the words.
    """

    def __init__(self, words, grid, word_positions):
        """
        Initializes the PuzzleSolver object.

        Args:
            words (list): A list of words in the word search.
            grid (list): The word search grid.
            word_positions (dict): Dictionary mapping each word to its starting position and direction.
                                   Format: {word: (x_start, y_start, dx, dy)}
        """
        self.words = words
        self.grid = grid
        self.word_positions = word_positions

    def solve_word_search(self):
        """
        Highlights all the letters of each word in the grid by adding red color codes.
        """
        for word in self.words: #similar 
            if word in self.word_positions:
                x_pos, y_pos, dx, dy = self.word_positions[word]

                # Highlight all letters in the word
                for i in range(len(word)):
                    new_x = x_pos + i * dx
                    new_y = y_pos + i * dy
                    self.grid[new_x][new_y] = f"\033[31m{word[i]}\033[0m"  # Colors the letter red

    def display_solved_grid(self):
        """
        Displays the grid with all the words highlighted.
        """
        print("\nSolved Word Search (All letters highlighted):")
        for row in self.grid:
            print(" ".join(row))

    def ask_for_solve(self):
        """
        Asks the user if they want the word search puzzle to be solved.
        This will be after the user says no to a hint.
        """
        while True:
            user_input = input("\nWould you like the word search to be solved? (Y/N): ").strip().upper()
            if user_input == "Y":
                print("Solving the puzzle...")
                self.solve_word_search()
                self.display_solved_grid()
                break
            elif user_input == "N":
                print("Alright, good luck solving it!")
                break
            else:
                print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
