import zmq
import json

with open('reviews.json', 'r') as file:
    reviews = json.load(file)

string_reviews = json.dumps(reviews)

def connect_to_review_service():
    context = zmq.Context()
    print("Client attempting to connect to server...")
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")
    print(f"Sending a request...")
    return socket

def get_all_reviews(socket):
    socket.send_string(string_reviews)
    print("The server sent back: ")
    try:
        return json.loads(string_reviews)
    except json.JSONDecodeError:
        print("Failed to decode reviews.")
        return []

def display_reviews(reviews):
    if not reviews:
        print("No reviews found.")
        return

    print("\n User Reviews:")
    for i, review in enumerate(reviews, start=1):
        print(f"\nReview {i}")
        print(f"User: {review.get('name', 'Unknown')}")
        print(f"Rating: {'⭐' * review.get('rating', 0)} ({review.get('rating', 0)}/5)")
        print(f"Review: {review.get('review', '[No review]')}")

def main():
    print("Welcome to Pet Adoption CLI!")
    socket = connect_to_review_service()

    while True:
        print("\nMain Menu:")
        print("1. View Reviews")
        print("2. Exit")

        choice = socket.recv_string()
        print(f"Received choice {choice}")

        if choice == "1":
            try:
                reviews = get_all_reviews(socket)
        
                display_reviews(reviews)
            except Exception as e:
                print(f"Error retrieving reviews: {e}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
