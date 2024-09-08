import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse

class TestCalculatorAPI():
    def test_calculate_add(self):
        url = "http://localhost:5000/calculate"
        payload = {
                    "operation": "add",
                    "operand1": 1,
                    "operand2": 1
        }

        response = requests.post(url, json=payload)
    
    def test_generated_code_test(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=1,operand2=1 ))
        assert isinstance(response, ResultResponse)
        assert response.result == 2

    def test_generated_code_test(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.SUBTRACT, operand1=1,operand2=1 ))
        assert isinstance(response, ResultResponse)
        assert response.result == 0

    def test_generated_code_test(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.MULTIPLY, operand1=2,operand2=4 ))
        assert isinstance(response, ResultResponse)
        assert response.result == 8

    def test_generated_code_test(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.DIVIDE, operand1=6,operand2=2 ))
        assert isinstance(response, ResultResponse)
        assert response.result == 3

    