# rewards_prog.py

# Global variable to store customer information
cust_list = []

class RewardsProgram:
    """A class to represent a customer's rewards program information."""

    def __init__(self, cust_name, phone, email):
        """Initialize the customer's name, phone, and email."""
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        """Print the customer's profile information."""
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        """Print a thank-you message for the customer."""
        print(f"Thank you, {self.cust_name}, for visiting our God like restaurant! If you dont come back, just know we know where you live!")

    def add_to_cust_list(self):
        """Add the customer's information to the global customer list."""
        cust_list.append((self.cust_name, self.phone, self.email))

#: Create instances of the RewardsProgram class
customer1 = RewardsProgram("Kailyn Mabon", "999-222-3333", "kailyn@yahoo.com")
customer2 = RewardsProgram("Cammeron Mabon", "000-333-5555", "cammeronmabon@gmail.com")
customer3 = RewardsProgram("Spongebob", "773-545-7789", "spongebobisyourlordandsavior@gmail.com")

# Run the methods for each customer
customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()

# Step 4: Print the contents of cust_list
print("\nCustomer List:")
for cust in cust_list:
    print(cust)