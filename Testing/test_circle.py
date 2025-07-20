import pytest
import math
from circle import Circle

class TestCircle:
    def setup_method(self):
        self.circle = Circle(5)

    def test_area(self):
        result = round(self.circle.area(),2)
        assert result == round(78.53981633974483,2)

    def test_circum(self):
        result = round(self.circle.circumference(),2)
        assert result == round(31.41592653589793,2)
    
    def test_diameter(self):
        result = self.circle.diameter()
        assert result == 10