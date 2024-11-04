# restaurants_enhanced.py

class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, rest_name, food_type):
        """Initialize the restaurant's name, food type, and additional attributes."""
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0  # Default attribute for number served
        self.customer_ratings = []  # Default attribute for customer ratings

    def describe_rest(self):
        """Print a description of the restaurant."""
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.rest_name} is open.")

    def add_num_served(self, num_customers):
        """Add the number of customers served today."""
        self.number_served += num_customers

    def print_num_served(self):
        """Print the total number of customers served."""
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        """Accept customer ratings and calculate the average rating."""
        while True:
            try:
                rating = int(input("How would you rate your experience today on a scale of 1-5? "))
                if rating < 1 or rating > 5:
                    raise ValueError("Rating must be between 1 and 5.")
                self.customer_ratings.append(rating)
                average_rating = sum(self.customer_ratings) / len(self.customer_ratings)
                print(f"Your rating was {rating}. The average rating for this restaurant is {average_rating:.2f}.")
                break  # Exit loop if a valid rating is provided
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter an integer between 1 and 5.")

# Step 3: Create instances of the Restaurant class with new names
restaurant1 = Restaurant("Kailyn's Lore", "Italian")
restaurant2 = Restaurant("Clap Yo Hands", "American")
restaurant3 = Restaurant("Come Smell What the Rock is Cooking", "Barbecue")

# Testing the new methods for restaurant1
restaurant1.print_num_served()  # Initial value
restaurant1.add_num_served(5)    # Add customers served
restaurant1.print_num_served()    # Updated value

restaurant1.customer_rating()      # Collect ratings
restaurant1.customer_rating()      # Collect another rating

# Testing for restaurant2
restaurant2.print_num_served()
restaurant2.add_num_served(3)
restaurant2.print_num_served()
restaurant2.customer_rating()

# Testing for restaurant3
restaurant3.print_num_served()
restaurant3.add_num_served(10)
restaurant3.print_num_served()
restaurant3.customer_rating()