# main.py

from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

def main():
    print(" Welcome to AI Travel Designer Agent!")

    # Step 1: Mood or interest input
    mood = input("What's your travel mood or interest? (adventure, relaxation, culture): ")

    # Step 2: DestinationAgent
    dest_agent = DestinationAgent()
    destinations = dest_agent.suggest_destinations(mood)
    print("\n Recommended destinations:")
    for i, dest in enumerate(destinations, 1):
        print(f"{i}. {dest}")

    # Step 3: Choose a destination
    choice = int(input("\nSelect a destination by number: "))
    selected_destination = destinations[choice - 1]

    # Step 4: BookingAgent
    booking_agent = BookingAgent()
    flights, hotels = booking_agent.book_travel(selected_destination)
    print(f"\n Available flights to {selected_destination}:")
    for f in flights:
        print(f"- {f}")
    print(f"\n Suggested hotels in {selected_destination}:")
    for h in hotels:
        print(f"- {h}")

    # Step 5: ExploreAgent
    explore_agent = ExploreAgent()
    attractions, food = explore_agent.explore_destination(selected_destination)
    print(f"\n Top attractions in {selected_destination}:")
    for a in attractions:
        print(f"- {a}")
    print(f"\n🍽️ Food experiences in {selected_destination}:")
    for f in food:
        print(f"- {f}")

    print("\n Your personalized travel plan is ready. Bon voyage!")

if __name__ == "__main__":
    main()
