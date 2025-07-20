import unittest
from unittest.mock import Mock

def my_function():
    return "Real Value"

class simple_mock(unittest.TestCase):
    def test_mocked_function(self):
        my_function=lambda:"Mocked Value"
        result=my_function()
        assert result=="Mocked Value"

