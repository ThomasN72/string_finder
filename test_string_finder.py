import unittest
from string_finder import string_finder


class TestStringFinder(unittest.TestCase):

    def test_string_finder_with_first_substring(self):
        # Arrange
        test_string = "My cat was missing today I hope she comes back. She was chased by the dog next door."
        params = ["cat", "dog", "chased"]
        # Act
        result = string_finder(test_string, params)
        # Assert
        self.assertEqual(
            result, "cat was missing today I hope she comes back. She was chased by the dog")

    def test_string_finder_with_second_substring(self):
        # Arrange
        test_string = "My cat was missing today I hope she comes back. She was chased by the dog next door. I love my cat."
        params = ["cat", "dog", "chased"]
        # Act
        result = string_finder(test_string, params)
        # Assert
        self.assertEqual(result, "chased by the dog next door. I love my cat")

    def test_string_finder_with_second_substring(self):
        # Arrange
        test_string = "My cat dog chased was missing today I hope she comes back. She was chased by the dog next door. I love my cat."
        params = ["cat", "dog", "chased"]
        # Act
        result = string_finder(test_string, params)
        # Assert
        self.assertEqual(result, "cat dog chased")

    def test_string_finder_with_no_result(self):
        # Arrange
        test_string = "My cat was missing today I hope she comes back. She was chased by the dog next door. I love my cat."
        params = ["catss"]
        # Act
        result = string_finder(test_string, params)
        # Assert
        self.assertEqual(result, "")

    def test_string_finder_with_no_params(self):
        # Arrange
        test_string = "My cat was missing today I hope she comes back. She was chased by the dog next door. I love my cat."
        params = []
        # Act
        result = string_finder(test_string, params)
        # Assert
        self.assertEqual(result, "")

    def test_string_finder_with_empty_string(self):
        # Arrange
        test_string = ""
        params = ["cat", "dog", "chased"]
        # Act
        result = string_finder(test_string, params)
        # Assert
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
