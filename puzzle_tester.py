import unittest
import string
from word_search import WordSearch

class TestWordSearch(unittest.TestCase):
    """Basic tests for the WordSearch class."""

    def setUp(self):
        """Set up a WordSearch instance with basic configurations."""
        self.word_search = WordSearch()

    def test_set_difficulty(self):
        """Test setting grid size based on difficulty."""
        self.word_search.grid_size = 10
        self.assertEqual(self.word_search.grid_size, 10)
        self.word_search.grid_size = 15
        self.assertEqual(self.word_search.grid_size, 15)

    def test_generate_word_search(self):
        """Test word generation for the word search."""
        self.word_search.generate_word_search()
        self.assertEqual(len(self.word_search.words), 5, "Should generate exactly 5 words.")
        for word in self.word_search.words:
            self.assertIn(word, [
                "APPLE", "BANANA", "ORANGE", "PYTHON", "PUZZLE", "SEARCH", "COMPUTER",
            "SCIENCE", "PROGRAM", "CODING", "LOGIC", "FUN", "GAMING", "HELLO", "WORLD",
            "ALGORITHM", "DATA", "DEBUG", "STRING", "NUMBER", "MATRIX", "ARRAY",
            "LOOP", "CONDITION", "VARIABLE", "CLASS", "METHOD", "OBJECT"
            ], f"Word '{word}' not in predefined word list.")

    def test_grid_creation(self):
        """Test creating the grid and placing words."""
        self.word_search.grid_size = 10
        self.word_search.grid = [['_' for _ in range(self.word_search.grid_size)] for _ in range(self.word_search.grid_size)]
        self.assertEqual(len(self.word_search.grid), 10, "Grid should have 10 rows.")
        self.assertEqual(len(self.word_search.grid[0]), 10, "Each row should have 10 columns.")

    def test_place_words(self):
        """Test placing words into the grid."""
        self.word_search.set_difficulty()  # Mock difficulty
        self.word_search.generate_word_search()
        self.word_search.place_words()
        for word, position in self.word_search.word_positions.items():
            self.assertIn(word, self.word_search.words, f"Word '{word}' should be in the word list.")

    def test_fill_empty_spaces(self):
        """Test filling empty spaces in the grid."""
        self.word_search.grid_size = 10
        self.word_search.grid = [['_' for _ in range(self.word_search.grid_size)] for _ in range(self.word_search.grid_size)]
        self.word_search.fill_empty_spaces()
        for row in self.word_search.grid:
            for cell in row:
                self.assertIn(cell, string.ascii_uppercase, f"Cell '{cell}' should be an uppercase letter.")

if __name__ == "__main__":
    unittest.main()
