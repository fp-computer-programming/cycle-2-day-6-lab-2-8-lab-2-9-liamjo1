# Liam O'Hara 9/23/2023

my_input = input("Enter number of points: ")
my_input = int(my_input)
if my_input <= 8:
    print("No Medal!")
elif my_input <= 11:
    print("Bronze Medal")
elif my_input <= 14:
    print("Silver Medal")
else:
    print("Gold Medal")