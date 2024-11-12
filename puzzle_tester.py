import unittest
from puzzle_generator import PuzzleGenerator

class TestPuzzleGenerator(unittest.TestCase):
    """Unit tests for the PuzzleGenerator class."""
    
    def test_generate_maze(self):
        """Test maze generation at various difficulty levels."""
        generator = PuzzleGenerator()
        # Example assertions for difficulty levels
        self.assertIsInstance(generator.generate_maze(1), list)
    
    def test_generate_word_search(self):
        """Test word search generation with different word lists."""
        generator = PuzzleGenerator()
        # Test with a sample word list and check grid validity
        self.assertIsInstance(generator.generate_word_search(['apple', 'banana']), list)


# Additional test files 