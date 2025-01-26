"""
Unit tests for error handling
"""

# pylint:disable=wrong-import-position

import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.getcwd())
from wrapworks.error_handling import eprint


class TestEprintFunction(unittest.TestCase):
    """Test Class for eprint"""

    def test_eprint_with_traceback(self):
        """Test the function with traceback"""
        try:
            1 / 0
        except ZeroDivisionError as e:
            with patch("wrapworks.error_handling.print") as mock_print, patch(
                "traceback.print_tb"
            ) as mock_print_tb:
                eprint(e, self.test_eprint_with_traceback, no_tracebacks=False)

                mock_print.assert_called_once()
                mock_print_tb.assert_called_once()

    def test_eprint_without_traceback(self):
        """Test the function without traceback"""
        try:
            a = 1
            b = "2"
            c = a + b
        except TypeError as e:
            with patch("wrapworks.error_handling.print") as mock_print, patch(
                "traceback.print_tb"
            ) as mock_print_tb:
                eprint(e, self.test_eprint_without_traceback, no_tracebacks=True)

                mock_print.assert_called_once()
                mock_print_tb.assert_not_called()


if __name__ == "__main__":
    unittest.main()
