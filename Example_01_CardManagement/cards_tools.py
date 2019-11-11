# record all cards' dict
card_list = []


def show_memu():

    """Show the Menu"""
    print("#" * 50)
    print("Welcome to cards manage system V1.0")
    print("1 to create a new card\n"
          "2 to show all cards\n"
          "3 to search and modify a card\n"
          "0 to exit the program")

    print("#" * 50)

def new_card():

    """add a new card"""

    print("=" * 50)
    # 1.Get information

    name_str = input("Name? ")
    qq_str = input("QQ? ")
    mob_str = input("MobilePhone? ")
    email_str = input("Email? ")

    # 2.Create a dict
    card_dict = {"name": name_str,
                 "qq": qq_str,
                 "mob": mob_str,
                 "email": email_str
    }

    # 3.Append the dict into list
    card_list.append(card_dict)
    print(card_list)

    # 4.tell the user that he create a new card successfully
    print("Congratulation! You create the %s's card!" % name_str)

def show_all():

    """show all cards' info"""

    print("=" * 50)
    print("Show all cards")
    # judge if it is an empty list
    if len(card_list) == 0:
        print("Empty Name List, Please create a new card first!")

        # if return triggered, codes behind won't be execute

        return

    for name in ["Name", "QQ", "MobilePhone", "Email"]:
        print(name, end="\t\t\t")

    print("")
    print("%" * 50)

    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["qq"],
                                        card_dict["mob"],
                                        card_dict["email"]))

def search_card():

    """search and modify a card"""

    # 1.notify the user to input the name he want
    find_name = input("The Name You Want? ")

    # 2.search the name thorough the list
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("Name\t\tQQ\t\tMobilePhone\t\tEmail")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["qq"],
                                            card_dict["mob"],
                                            card_dict["email"]))

            # TODO(bamboo) Modify a card
            deal_card(card_dict)

            break

    else:
        print("Sorry. We didn't find %s" % find_name)

    print("=" * 50)

def deal_card(find_dict):

    action_str = input("[1]Modify [2]Delete [0]Back to Main menu")

    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "name")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ?")
        find_dict["mob"] = input_card_info(find_dict["mob"], "MobilePhone?")
        find_dict["email"] = input_card_info(find_dict["email"], "Email?")

        print("Modify the card successfully!")

    elif action_str == "2":

        card_list.remove(find_dict)
        print("Delete the card successfully!")

def input_card_info(dict_value, tip_message):
    """to output a new value or the original value

    :param dict_value: The original value
    :param tip_message: The new value
    :return:
    """
    # 1. notify the user
    result_str = input(tip_message)

    # 2.judge if it is empty
    if len(result_str) > 0:
        return result_str

    # 3.judge
    else:
        return dict_value

