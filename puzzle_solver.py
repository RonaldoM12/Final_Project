class PuzzleSolver:
    """
    Solves puzzles by providing solutions based on puzzle data.

    Methods:
        solve_word_search(word_search_data, word): Finds a word in the word search grid.
    """
    
    def solve_word_search(self, word_search_data: list, word: str) -> tuple:
        """
        Locates a specified word within the word search puzzle.

        Args:
            word_search_data (list): A 2D grid representing the word search puzzle.
            word (str): The word to locate within the grid.

        Returns:
            tuple: The starting coordinates of the word in the grid.
        """

        rows = len(word_search_data)
        cols = len(word_search_data[0]) if rows > 0 else 0
        word_length = len(word)

        directions = [ (0, 1) #right
                      , (1, 0) #down 
                      , (0, -1) #left 
                      , (-1, 0) #up
                      , (1, 1) #Diagonal down right
                      , (1, -1) #Diagonal down left
                      , (-1, -1) #Diagonal up - left
                      , (-1, 1) #diagonal up - right
                      ]
        def is_valid_position(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def search_from_position(row, col, direction):
            for i in range(word_length):
                new_row = row + i * direction[0]
                new_col = col + i * direction[i]
                if not is_valid_position(new_row, new_col) or word_search_data[new_row][new_col] != word[i]:
                    return False
                return True
            
        for row in range(rows):
            for col in range(cols):
                if word_search_data[row][col] == word[0]:
                    for direction in directions:
                        return(row, col)
        # Search for the word in the grid and return its starting position if found
        return(-1,-1)
    
    def ask_for_solve(self, word_search_data, words):
        """
        Asks the user if they want the word search puzzle solved.

        Args:
            word_search_data (list): The word search grid.
            words (list): List of words to be solved.
        """
        while True:
            user_input = input("\nWould you like the word search to be solved? (Y/N): ").strip().upper()
            if user_input == "Y":
                print("Solving the puzzle...")
                for word in words:
                    result = self.solve_word_search(word_search_data, word)
                    if result != (-1, -1):
                        print(f"Word '{word}' found starting at position {result}.")
                    else:
                        print(f"Word '{word}' not found in the grid.")
                break
            elif user_input == "N":
                print("Alright, good luck solving it!")
                break
            else:
                print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
