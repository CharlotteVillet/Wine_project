import requests

url = "http://127.0.0.1:5000/predict"

# Example of input with one single input
simple_input = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

res_simple_input = requests.post(url, json=simple_input)
assert res_simple_input.status_code == 200
print(res_simple_input.json())