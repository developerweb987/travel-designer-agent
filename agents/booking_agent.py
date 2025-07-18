# agents/booking_agent.py

from tools.travel_tools import get_flights, suggest_hotels

class BookingAgent:
    def book_travel(self, destination):
        flights = get_flights(destination)
        hotels = suggest_hotels(destination)
        return flights, hotels
