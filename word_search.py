import random
import string

class WordSearch:
    """
    A class to generate and manage word search puzzles.
    
    Attributes:
        grid_size (int): The size of the word search grid.
        grid (list): A 2D list representing the grid for the word search puzzle.
        words (list): A list of words to be placed in the grid.
    """
    
    def __init__(self, grid_size=15):
        """
        Initializes the WordSearch object with a specified grid size.

        Args:
            grid_size (int): The size of the grid. Default is 15.
        """
        self.grid_size = grid_size
        self.grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]
        self.words = []  #To store the list of words

    def generate_word_search(self):
        """
        Generates a list of random words from a predefined list and stores them
        in the class for placement in the word search puzzle.

        Randomly selects 5 unique words from a predefined list of words.
        """
        word_list = [
            "APPLE", "BANANA", "ORANGE", "PYTHON", "PUZZLE", "SEARCH", "COMPUTER",
            "SCIENCE", "PROGRAM", "CODING", "LOGIC", "FUN", "GAMING", "HELLO", "WORLD",
            "ALGORITHM", "DATA", "DEBUG", "STRING", "NUMBER", "MATRIX", "ARRAY",
            "LOOP", "CONDITION", "VARIABLE", "CLASS", "METHOD", "OBJECT"
        ]
        self.words = random.sample(word_list, 5)  #Ensure unique words
        print("Random Words:", self.words)

    def create_grid(self):
        """
        Displays the current state of the grid.

        Prints the grid row by row, with each cell separated by a space.
        """
        for x in range(self.grid_size):
            print(' '.join(self.grid[x]))

    def place_words(self):
        """
        Places the generated words into the grid in random directions.

        Words are placed in one of four possible directions:
            - left-right (horizontal)
            - up-down (vertical)
            - diagonal-down (diagonally downward)
            - diagonal-up (diagonally upward)
        
        Words are placed only if they fit within the grid bounds and do not
        conflict with other placed words. If a word cannot be placed within
        100 attempts, it is skipped.
        """
        directions = ['left-right', 'up-down', 'diagonal-down', 'diagonal-up']

        for word in self.words:
            word_length = len(word)  #Check the length of the word so it doesn't go off the grid
            placed = False
            attempts = 0  #Add a counter for attempts

            while not placed and attempts < 100:  #Limit to 100 attempts
                direction = random.choice(directions)
                dx, dy = 0, 0

                if direction == 'left-right':
                    dx, dy = 0, 1
                elif direction == 'up-down':
                    dx, dy = 1, 0
                elif direction == 'diagonal-down':
                    dx, dy = 1, 1
                elif direction == 'diagonal-up':
                    dx, dy = -1, 1

                #Random starting position
                x_pos = random.randint(0, self.grid_size - 1)
                y_pos = random.randint(0, self.grid_size - 1)

                #Check if the word falls out of the area
                ending_x = x_pos + (word_length - 1) * dx
                ending_y = y_pos + (word_length - 1) * dy

                if ending_x < 0 or ending_x >= self.grid_size or ending_y < 0 or ending_y >= self.grid_size:
                    attempts += 1
                    continue

                #Check if the word overlaps correctly or fits
                not_placed = False
                for i in range(word_length):
                    new_x = x_pos + i * dx
                    new_y = y_pos + i * dy

                    new_position = self.grid[new_x][new_y]
                    if new_position != '_':
                        if new_position == word[i]:
                            continue
                        else:
                            not_placed = True
                            break

                if not_placed:
                    attempts += 1
                    continue
                else:
                    # Place the word
                    for i in range(word_length):
                        new_x = x_pos + i * dx
                        new_y = y_pos + i * dy
                        self.grid[new_x][new_y] = word[i]
                    placed = True

            if not placed:
                print(f"Failed to place the word: {word}")
                
    def fill_empty_spaces(self):
        """
        Fills empty spaces in the grid with random letters.

        Any cell in the grid that contains '_' is replaced with a random
        uppercase letter.
        """
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.grid[row][col] == '_':
                    self.grid[row][col] = random.choice(string.ascii_uppercase)
                                    
if __name__ == "__main__":
    ws = WordSearch()
    ws.generate_word_search()
    ws.place_words()
    ws.fill_empty_spaces()
    ws.create_grid()
