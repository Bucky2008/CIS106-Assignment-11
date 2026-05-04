# Array (list) of last names
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

# Parallel array of scores
scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]


# INPUT PHASE
# (arrays above)


# PROCESS PHASE
# Function to find highest and lowest
def find_high_low(names, scores):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i

        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    return high_index, low_index


# OUTPUT PHASE
high_i, low_i = find_high_low(last_names, scores)

print("Highest:", last_names[high_i], "-", scores[high_i])
print("Lowest:", last_names[low_i], "-", scores[low_i])