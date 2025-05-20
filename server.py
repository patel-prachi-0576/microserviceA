import zmq
import json
import time

# Load reviews from JSON file
with open('reviews.json') as f:
    reviews = json.load(f)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Review microservice running on port 5555...")

while True:
    message = socket.recv_string()
    print(f"Received request from client: {message}")

    if message == "get_all":
        time.sleep(3)
        socket.send_string(json.dumps(reviews))
    else:
        socket.send_string("INVALID_COMMAND")
