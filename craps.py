from random import randint

print("Welcome to Dice")
print("Please pick your game")
for i in range(6):
    print(str(i+1) + ". " + str(i+1) + "'s away")

away_choice = int(input("Choose your game: "))
print(str(away_choice) + "'s away it is!")

num_of_players = int(input("How many players in the game: "))
busted = [False for i in range(num_of_players)]
total = [0 for i in range(num_of_players)]
the_number = 0
for i in range(num_of_players):
    remaining_rolls = 5
    print("Player " + str(i+1) + "'s turn")
    while remaining_rolls:
        if i != 0:
            print("Rolling..." + str(away_choice) + "'s the game " + str(the_number) + "'s the number")
        else:
            print("Rolling..." + str(away_choice) + "'s the game")
        values = []
        for j in range(remaining_rolls):
            values.append(randint(1,6))
            print("Die #" + str(j+1) + ": ", values[j])
        remaining_rolls -= 1
        keep_choice = int(input("Select dice to keep (you must keep at least one):"))
        if values[keep_choice-1] != away_choice:
            total[i] += values[keep_choice-1]
            if (i != 0 and total[i] > the_number):
                print("Nope, you're done!")
                break
        print("Player " + str(i+1) + " your total is: ", total[i])
    if (i == 0 or the_number > total[i]):
        the_number = total[i]

print("Results:")
for i in range(num_of_players):
    print("Player " + str(i+1) + ": ", total[i])
print("Player " + str(total.index(min(total))+1) + " wins!")







