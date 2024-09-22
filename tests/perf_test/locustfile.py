from locust import HttpUser, task, between
import json

class CalculatorUser(HttpUser):

    wait_time = between(2,4)

    def on_start(self):
        pass

    @task(2)
    def add(self):
        add = {
            "operation": "add",
            "operand1": 100,
            "operand2": -200
        }
        with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == -100:
                response.failure(f"Expected result to be 2 but was {response_data['result']}")

    @task
    def subtract(self):
        body = {
            "operation": "subtract",
            "operand1": 1,
            "operand2": 1
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=body) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 0:
                response.failure(f"Expected result to be 0 but was {response_data['result']}")

    @task
    def multiply(self):
        body = {
            "operation": "multiply",
            "operand1": 2,
            "operand2": 3
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=body) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 6:
                response.failure(f"Expected result to be 6 but was {response_data['result']}")

    @task
    def divide(self):
        body = {
            "operation": "divide",
            "operand1": 6,
            "operand2": 2
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=body) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 3:
                response.failure(f"Expected result to be 3 but was {response_data['result']}")

if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)