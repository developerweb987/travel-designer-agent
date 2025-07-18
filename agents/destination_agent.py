# agents/destination_agent.py

class DestinationAgent:
    def suggest_destinations(self, mood_or_interest):
        mood_map = {
            "adventure": ["Nepal", "Peru", "New Zealand"],
            "relaxation": ["Maldives", "Bali", "Hawaii"],
            "culture": ["Rome", "Kyoto", "Istanbul"]
        }
        return mood_map.get(mood_or_interest.lower(), ["Paris", "New York", "Dubai"])
