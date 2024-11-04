# restaurants.py

class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, rest_name, food_type):
        """Initialize the restaurant's name and food type."""
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        """Print a description of the restaurant."""
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.rest_name} is open.")

# Create instances of the Restaurant class
restaurant1 = Restaurant(" Kailyns Burgers", "Italian")
restaurant2 = Restaurant("Top Tier", "Japanese")
restaurant3 = Restaurant("Queso Dill", "Mexican")

# Call describe_rest() and rest_open() for each instance
restaurant1.describe_rest()  # Outputs: Kailyns Burger serves Italian.
restaurant1.rest_open()       # Outputs: Kailyns Burger is open.

restaurant2.describe_rest()  # Outputs: Top Tier serves Japanese.
restaurant2.rest_open()       # Outputs: Top Tier is open.

restaurant3.describe_rest()  # Outputs: Queso Dill serves Mexican.
restaurant3.rest_open()       # Outputs: Queso Dill is open.