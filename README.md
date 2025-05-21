
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
```bash
socket.send_string("get_all")
```

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

(https://drive.google.com/file/d/1zzvgCYKBhQimFWPnOsYvBwLm033NKUkW/view?usp=sharing)

## Mitigation Plan

1.	I implemented microservice A for Leonardo.

2.	The microservice is complete and fully functional. I tested it locally, and it is ready to be integrated by Leonardo.


3.	The microservice will be accessible through the Github repository: https://github.com/patel-prachi-0576/microserviceA.git

4.	If Leonardo cannot access or call my microservice, then he should contact me directly on Discord. I’m available any day of the week, but I will most likely respond in the evenings. I will prioritize fixing any issues that come up. Do let me know two days before the microservice implementations are due so that I have time to upload any changes.


5.	Things necessary to know before implementation:
•	This microservice returns user reviews over a ZeroMQ socket
•	It loads reviews from a local reviews.json file. The JSON file must be in the same directory as the server file.
•	Make sure that any new reviews added are in the format of a dictionary in the JSON file. An example is shown in the README file on Github.
•	Python must be installed
•	The microservice will start and bind to tcp://*:5555



