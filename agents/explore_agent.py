# agents/explore_agent.py

from tools.travel_tools import suggest_attractions, suggest_food

class ExploreAgent:
    def explore_destination(self, destination):
        attractions = suggest_attractions(destination)
        food = suggest_food(destination)
        return attractions, food
