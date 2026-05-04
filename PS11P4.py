# INPUT PHASE
# Load data from file into arrays
last_names = []
averages = []

file = open("players.txt", "r")

for line in file:
    data = line.strip().split()
    last_names.append(data[0])
    averages.append(float(data[1]))

file.close()


# PROCESS PHASE
# Function to display arrays
def display_players(names, avgs):
    print("Players and Batting Averages:")
    for i in range(len(names)):
        print(names[i], "-", avgs[i])


# Function to search for a player
def search_player(names, avgs, target):
    for i in range(len(names)):
        if names[i].lower() == target.lower():
            print("Found:", names[i], "-", avgs[i])
            return
    print("Name not found")


# OUTPUT PHASE
display_players(last_names, averages)

while True:
    user_input = input("\nEnter last name (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    search_player(last_names, averages, user_input)