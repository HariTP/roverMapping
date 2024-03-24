import unittest
from rover_mapping import Coordinates, Position, move

class TestRoverMapping(unittest.TestCase):
    # Testcase 1: Example 1 (provided in the assignment)
    def test_example_1(self):
        upper_right_coordinates = Coordinates(5, 5)
        curr_position = Position(1, 2, "N")
        instructions = "LMLMLMLMM"
        expected_result = "1 3 N"
        self.assertEqual(move(upper_right_coordinates, curr_position, instructions), expected_result)

    # Testcase 2: Example 2 (provided in the assignment)
    def test_example_2(self):
        upper_right_coordinates = Coordinates(5, 5)
        curr_position = Position(3, 3, "E")
        instructions = "MMRMMRMRRM"
        expected_result = "5 1 E"
        self.assertEqual(move(upper_right_coordinates, curr_position, instructions), expected_result)

    # Testcase 3: Trying to move rover outside the boundary from upper-right corner of the plateau
    def test_move_rover_outside_boundary_upper_right_corner(self):
        plateau_size = Coordinates(5, 5)
        initial_position = Position(5, 5, "N")
        instructions = "M"
        expected_result = "5 5 N"
        self.assertEqual(move(plateau_size, initial_position, instructions), expected_result)

    # Testcase 4: Trying to move rover outside the boundary from lower-left corner of the plateau
    def test_move_rover_outside_boundary_lower_left_corner(self):
        plateau_size = Coordinates(5, 5)
        initial_position = Position(0, 0, "S")
        instructions = "M"
        expected_result = "0 0 S"
        self.assertEqual(move(plateau_size, initial_position, instructions), expected_result)

    # Testcase 5: Trying to move rover outside the boundary from upper-left corner of the plateau
    def test_move_rover_outside_boundary_upper_left_corner(self):
        plateau_size = Coordinates(5, 5)
        initial_position = Position(0, 5, "W")
        instructions = "M"
        expected_result = "0 5 W"
        self.assertEqual(move(plateau_size, initial_position, instructions), expected_result)

    # Testcase 6: Trying to move rover outside the boundary from lower-right corner of the plateau
    def test_move_rover_outside_boundary_lower_right_corner(self):
        plateau_size = Coordinates(5, 5)
        initial_position = Position(5, 0, "E")
        instructions = "M"
        expected_result = "5 0 E"
        self.assertEqual(move(plateau_size, initial_position, instructions), expected_result)

    # Testcase 7: Starting from the upper-left corner and moving inward
    def test_move_upper_left_corner(self):
        plateau_size = Coordinates(5, 5)
        initial_position = Position(0, 5, "N")
        instructions = "LLM"
        expected_result = "0 4 S"
        self.assertEqual(move(plateau_size, initial_position, instructions), expected_result)

    # Testcase 8: Starting from the upper-right corner and moving inward
    def test_move_upper_right_corner(self):       
        plateau_size = Coordinates(5, 5)
        initial_position = Position(5, 5, "N")
        instructions = "LLMLL"
        expected_result = "5 4 N"
        self.assertEqual(move(plateau_size, initial_position, instructions), expected_result)

    # Testcase 9: Starting from the lower-left corner and moving inward
    def test_move_lower_left_corner(self):
        plateau_size = Coordinates(5, 5)
        initial_position = Position(0, 0, "N")
        instructions = "M"
        expected_result = "0 1 N"
        self.assertEqual(move(plateau_size, initial_position, instructions), expected_result)
    
    # Testcase 10: Starting from the lower-right corner and moving inward
    def test_move_lower_right_corner(self):
        plateau_size = Coordinates(5, 5)
        initial_position = Position(5, 0, "N")
        instructions = "M"
        expected_result = "5 1 N"
        self.assertEqual(move(plateau_size, initial_position, instructions), expected_result)

if __name__ == '__main__':
    unittest.main()
