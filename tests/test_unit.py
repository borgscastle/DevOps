from BE.calculator_helper import CalculatorHelper
import pytest

class BaseClass(): # Kan läggas i egen fil och importeras. 
    def setup_method(self):
        self.calculator = CalculatorHelper()

    def teardown_method(self):
        self.calculator = None

class TestCalculator(BaseClass):

    def test_first(self):
        pass

    def test_add(self):
    #arrange
    #    calculator = CalculatorHelper()
    #action
        value = self.calculator.add(1,1)
    #assert 
        assert value == 2

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 2, 4),       # Testfall 1 a + b = expected i detta fall 2 * 2 = 4
            (3, 5, 15),      # Testfall 2
            (0, 10, 0),      # Testfall 3
            (-1, -1, 1),     # Testfall 4
            (7, 3, 21)       # Testfall 5
        ]
    )
    def test_multi(self, a, b, expected):
        # Action
        value = self.calculator.multiply(a, b)
        # Assert
        assert value == expected

    def test_sub(self):
    #arrange
    #   calculator = CalculatorHelper()
    #action
        value = self.calculator.subtract(3,1)
    #assert 
        assert value == 2

    def test_div(self):
    #arrange
    #    calculator = CalculatorHelper()
    #action
        value = self.calculator.divide(2,2)
    #assert 
        assert value == 1

    def test_div_with_zero(self):
    #arrange
    #    calculator = CalculatorHelper()
    #action
        with pytest.raises(ZeroDivisionError) as exinfo:
            value = self.calculator.divide(4,0)
        # Assert
        assert "division by zero" in str(exinfo.value), "Expected exception"


