from random import seed
from random import randint

print("Rolling...")
value_1 = randint(1,6)
value_2 = randint(1,6)
print(value_1)
print(value_2)
total = value_1 + value_2
print(total)

if (total == (7 or 11)):
    print("Boom, you win")
elif (total == (2 or 3 or 12)):
    print("You lose, you suck")
else:
    print("Keep it movin sucka")


