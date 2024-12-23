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
    
    def __init__(self):
        """
        Initializes the WordSearch object with a specified grid size.

        Args:
            grid_size (int): The size of the grid.
        """
        self.grid_size = None
        self.grid = None
        #self.grid_size = grid_size 
        #self.grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)] #will replace underscores with letters later
        self.words = []  #To store the list of words
        self.word_positions = {} #This is for our hint and solver logic
    
    def set_difficulty(self):
        """
        Asks the user what difficulty level they want and sets the grid size accordingly.
        """
        while True:
            difficulty = input("What Difficulty would you like(Easy, Medium, Hard, Impossible): ").lower() #.lower() to avoid case errors
            if difficulty == "easy":
                self.grid_size = 10
                break
            elif difficulty == "medium":
                self.grid_size = 15
                break
            elif difficulty == "hard":
                self.grid_size = 20
                break
            elif difficulty == "impossible":
                self.grid_size = 50
                break
            else:
                print("Invalid Difficulty Level Try Again:")
        self.grid = [['_' for _ in range(self.grid_size)] for _ in range(self.grid_size)] #Will replace underscores with letters later
        
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
        print("Find These Words:", self.words) #this is to check what words were given

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
            attempts = 0  #Add a counter for attempts so no infinite loops

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
                    if new_position != '_': #if the grid cell is empty the word can be placed
                        if new_position == word[i]:
                            continue
                        else:
                            not_placed = True #if it cant be placed go to the next segment
                            break

                if not_placed: 
                    attempts += 1 #Keep trying you have 100 attempts
                    continue
                else:
                    #Past this point the word can be placed!
                    for i in range(word_length): #Place the word based on its direction
                        new_x = x_pos + i * dx #placing each character one by one
                        new_y = y_pos + i * dy
                        self.grid[new_x][new_y] = word[i]
                        
                    self.word_positions[word] = (x_pos, y_pos, dx, dy) #Saves the words position in the grid
                    placed = True #Marks the word as placed

            if not placed:
                print(f"Failed to place the word: {word}") #test case for any random errors in placing words
                
    def fill_empty_spaces(self):
        """
        Fills empty spaces in the grid with random letters.

        Any cell in the grid that contains '_' is replaced with a random
        uppercase letter.
        """
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.grid[row][col] == '_': #replacing all underscores 
                    self.grid[row][col] = random.choice(string.ascii_uppercase)#getting random letters

#Testing for the output
"""                         
if __name__ == "__main__":
    ws = WordSearch()
    ws.set_difficulty()
    ws.generate_word_search()
    ws.place_words()
    ws.fill_empty_spaces()
    ws.create_grid()
"""
