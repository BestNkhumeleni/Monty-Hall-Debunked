import random

# Represents the door from which the prize is behind
dealer = random.randrange(0, 3)

# Choice of the contestant
contestant = random.randrange(0, 3)

# Tracks the number of times the contestant guesses correctly
counter = 0

# Simulate the Monty Hall problem for a million iterations
for i in range(1000000):
    # Host (dealer) opens a door with a goat that was not chosen by the contestant
    doors_with_goats = [door for door in range(
        3) if door != contestant and door != dealer]
    door_opened = random.choice(doors_with_goats)

    # Contestant switches to the other unopened door
    remaining_doors = [door for door in range(
        3) if door != door_opened and door != contestant]
    contestant = remaining_doors[0]

    # Check if the contestant's final choice is the door with the prize
    if contestant == dealer:
        counter += 1

# Calculate and print the probability
probability = counter / 1000000 * 100
print(probability, "%")
