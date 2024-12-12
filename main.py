import argparse
from word_search import WordSearch
from puzzle_solver import PuzzleSolver
from hint_provider import HintProvider

def run_puzzle_game():
    """
    Runs the puzzle game based on command-line inputs. Integrates with other modules to generate
    and solve puzzles, provide hints, and display results.
    
    Note:
        This function involves user input/output and requires a human testing procedure.
    """
    # Word Search Puzzle goes here
    ws = WordSearch()
    ws.set_difficulty()
    ws.generate_word_search()
    ws.place_words()
    ws.fill_empty_spaces()
    ws.create_grid()
    
    #Hint Provider and Solver for Word Search goes here
    hint_provider = HintProvider(ws.words, ws.grid, ws.word_positions)
    puzzle_solver = PuzzleSolver(ws.words, ws.grid, ws.word_positions)
    
    hint_provider.ask_for_hint()
    puzzle_solver.ask_for_solve()       
           
            
if __name__ == "__main__":
    run_puzzle_game()
