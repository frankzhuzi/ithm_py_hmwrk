#! /usr/bin/python3

# 1,2,3 action to cards
# 0 to exit
# others are error
# pass: take a place to keep the process runs well

import cards_tools

while True:

    # TODO(bamboo) Description of the functions
    cards_tools.show_memu()

    action_str = input("What action you wanna take")
    print("You choice is [%s]" % action_str)

    if action_str in ["1", "2", "3"]:

        if action_str == "1":
            cards_tools.new_card()

        elif action_str == "2":
            cards_tools.show_all()

        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":
        print("Nice to meet you! See you later!")
        break

    else:
        print("Error Input, Choose again")

# while True:




  #  if input1 = "0":
      #  break
