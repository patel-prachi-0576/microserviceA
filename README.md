
# Microservice A

This microservice provides access to user reviews for a pet adoption CLI application. The service uses ZeroMQ to send and receive data over a TCP socket.


## Overview
- Protocol: ZeroMQ
- Socket Type: REQ or REP
- Port: 5555
- Data Format: JSON
## Request Data
To request all reviews, the client must send a string

Code Example:

socket.send_string("get_all")
## Receive Data
The response from the microservice will be a JSON-encoded string representing a list of reviews. Each review is a dictionary with these keys:
- "user" (string): name of the reviewer
- "rating" (integer): number from 1 to 5
- "review" (string): the written review
Example of a review:
```bash
[

    {
    
        "user": "Patrick Star",

        "rating": 4

        "review": "The process was great overall, but it could be a faster process."
    }

]
```

Code example:
```bash
message = socket.recv_string()
reviews = json.loads(message)

for review in reviews:
    print(f"{review['user']} rated {review['rating']}/5: {review['review']}")
```

Supported commands only include "get_all". Any other message will get the result "INVALID_COMMAND"
## UML Diagram

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


