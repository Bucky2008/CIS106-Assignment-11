# Array (list) of 10 last names
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# Function to display names
def display_names(names):
    print("Names:")
    for name in names:
        print(name)

# Function to display names in reverse order
def display_reverse(names):
    print("\nNames in reverse:")
    for name in reversed(names):
        print(name)

# Call functions
display_names(last_names)
display_reverse(last_names)