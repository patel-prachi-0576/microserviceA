import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Request all reviews
socket.send_string("get_all")
message = socket.recv_string()
reviews = json.loads(message)

print("All reviews:")
for review in reviews:
    print(review)

# Request specific review by ID
socket.send_string("get_id:2")
message = socket.recv_string()

if message == "NOT_FOUND":
    print("Review not found.")
elif message.startswith("ERROR"):
    print("Error:", message)
else:
    review = json.loads(message)
    print("Review with ID 2:", review)

