import argparse
from word_search import WordSearch
#from maze_builder import Maze
from hint_provider import HintProvider

def parse_args() -> dict:
    """
    Parses command-line arguments for configuring the puzzle type, difficulty, and hints.

    Returns:
        dict: Dictionary containing parsed arguments (puzzle type, difficulty level, etc.).
    """
    #Parse arguments for type of puzzle, difficulty, and hint requests
    parser = argparse.ArgumentParser(description="Puzzle Generator")
    #Define arguments here
    return vars(parser.parse_args())

def run_puzzle_game():
    """
    Runs the puzzle game based on command-line inputs. Integrates with other modules to generate
    and solve puzzles, provide hints, and display results.
    
    Note:
        This function involves user input/output and requires a human testing procedure.
    """
    while True:
        puzzle_type = input("What type of puzzle would you like? (Word Search/Maze): ").lower()
        if puzzle_type == "word search":
            # Word Search Puzzle goes here
            ws = WordSearch()
            ws.set_difficulty()
            ws.generate_word_search()
            ws.place_words()
            ws.fill_empty_spaces()
            ws.create_grid()
            
            #Hint Provider for Word Search goes here
            hint_provider = HintProvider(ws.words, ws.grid, ws.word_positions)
            hint_provider.ask_for_hint()
            
            #Word Search Solver goes here
            #word_finder = solve_maze()
            break
        
        elif puzzle_type == "maze":
            #Maze Puzzle code goes here 
            pass
            
        else:
            print("Invalid input. Please enter 'Word Search' or 'Maze'.")            
            
if __name__ == "__main__":
    run_puzzle_game()
