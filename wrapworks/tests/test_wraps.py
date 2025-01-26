"""
Unit tests for wraps
"""

# pylint:disable=wrong-import-position

import os
import sys
import unittest
from unittest.mock import patch
import time

sys.path.append(os.getcwd())
from wrapworks.wraps import timeit, tryexcept, retry


class TestTimeIt(unittest.TestCase):
    """Test Class for timeit"""

    def test_timeit_decorator(self):
        """Check if the time is being print"""

        @timeit()
        def test_function():
            time.sleep(1)

        with patch("wrapworks.wraps.print") as mock_print:
            test_function()

        self.assertEqual(mock_print.call_count, 2)


class TestTryExcept(unittest.TestCase):
    """Test Class for tryexcept"""

    def test_custom_return(self):
        """Test for custom return"""

        @tryexcept(default_return="Customer return")
        def test_function():
            raise ValueError()

        result = test_function()
        self.assertEqual(result, "Customer return")

    def test_good_return(self):
        """Test if the function return the child's return"""

        @tryexcept()
        def test_function():
            return 5

        result = test_function()
        self.assertEqual(result, 5)

    def test_print(self):
        """Test if the function prints the error"""

        @tryexcept()
        def test_function():
            raise ValueError()

        with patch("wrapworks.wraps.print") as mock_print:
            _ = test_function()

        mock_print.assert_called_once()


class TestRetryOnException(unittest.TestCase):
    """Test Class for retry"""

    def test_print_count(self):
        """Test for print count"""

        @retry(max_retries=3, delay=0)
        def test_function():
            raise ValueError()

        with patch("wrapworks.wraps.print") as mock_print:
            result = test_function()

        self.assertEqual(mock_print.call_count, 4)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
