# tools/travel_tools.py

def get_flights(destination):
    return [
        f"Flight A to {destination} - $300",
        f"Flight B to {destination} - $280",
        f"Flight C to {destination} - $350"
    ]

def suggest_hotels(destination):
    return [
        f"Grand Hotel {destination}",
        f"Budget Inn {destination}",
        f"Luxury Suites {destination}"
    ]

def suggest_attractions(destination):
    return [
        f"{destination} Museum",
        f"{destination} Park",
        f"{destination} Historic District"
    ]

def suggest_food(destination):
    return [
        f"{destination} Street Food Tour",
        f"Top Restaurants in {destination}",
        f"Local Cuisine Specialties in {destination}"
    ]
