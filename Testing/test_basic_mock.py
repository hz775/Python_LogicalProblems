import unittest
from unittest.mock import Mock

class simple_mock(unittest.TestCase):
    def test_verify_simple_mock(self):

        my_mock=Mock()
        my_mock.return_value=14
        result=my_mock()
        assert result==14
    

