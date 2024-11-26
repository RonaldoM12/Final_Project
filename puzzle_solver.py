class PuzzleSolver:
    """
    Solves different types of puzzles by providing solutions based on puzzle data.

    Methods:
        solve_maze(maze_data): Solves a maze and returns a solution path.
        solve_word_search(word_search_data, word): Finds a word in the word search grid.
    """
    
    def solve_maze(self, maze_data: list) -> list:
        """
        Solves a maze by finding a path from start to end.

        Args:
            maze_data (list): A 2D list representing the maze layout.

        Returns:
            list: A list of coordinates representing the path through the maze.
        """
        # Implement pathfinding algorithm (e.g., BFS or DFS) to find solution path
        pass
    
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