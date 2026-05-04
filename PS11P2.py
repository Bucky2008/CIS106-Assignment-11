# Array (list) of 10 last names
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# Parallel array of exam scores
scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]


# INPUT PHASE
# (arrays above)


# PROCESS PHASE
# Function to display names with scores
def display_names(names, scores):
    print("Names:")
    for i in range(len(names)):
        print(names[i], "-", scores[i])

# Function to display names in reverse order with scores
def display_reverse(names, scores):
    print("\nNames in reverse:")
    for i in range(len(names)-1, -1, -1):
        print(names[i], "-", scores[i])


# OUTPUT PHASE
# Call functions
display_names(last_names, scores)
display_reverse(last_names, scores)