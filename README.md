# microserviceA

# This microservice provides access to user reviews for a pet adoption CLI application. The service uses ZeroMQ to send and receive data over a TCP socket.

# PROTOCOL OVERVIEW
# Protocol: ZeroMQ
# Socket Type: REQ or REP
# Port: 5555
# Data Format: JSON


# How to request data
# To request all reviews, the client must send a string
socket.send_string("get_all")

# How to receive data
# The response from the microservice will be a JSON-encoded string representing a list of reviews. Each review is a dictionary with these keys:
# "user" (string): name of the reviewer
# "rating" (integer): number from 1 to 5
# "review" (string): the written review
# Example of a review:
[
  {
    "user": "Patrick Star",
    "rating": 4
    "review": "The process was great overall, but it could be a faster process."
  }
]

# Example Python code to receive data
message = socket.recv_string()
reviews = json.loads(message)

for review in reviews:
    print(f"{review['user']} rated {review['rating']}/5: {review['review']}")

# Supported commands only include "get_all". Any other message will get the result "INVALID_COMMAND"


![uml screenshot](https://github.com/user-attachments/assets/29a7e656-2d10-46ec-99c4-6f329a8f8e2c)
