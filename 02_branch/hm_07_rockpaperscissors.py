import random
choice = int(input('Rock1 Scissors2 Paper3'))
computer = random.randint(1,3)
print('Players choice is %d - Computer choice is %d' % (choice,computer))
if choice == computer:
    print('Even!')
elif ((choice == 1 and computer == 2)
          or (choice == 2 and computer == 3)
          or (choice == 3 and computer == 1)):

    print("Player wins!")
else:
    print("Player sucks! Computer wins!")