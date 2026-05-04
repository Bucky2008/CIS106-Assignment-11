# Question 5 modification
def search_player(names, avgs, target):
    for i in range(len(names)):
        if names[i].lower() == target.lower():
            print("Found:", names[i], "-", avgs[i])
            return
    print("Name not found")