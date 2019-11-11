
def print_info(name, title = "classmate", gender=True):
    """

    :param title: The identity
    :param name: Classmates' name
    :param gender: True for male, False for female
    """

    gender_text = "Boy"

    if not gender:
        gender_text = "Girl"

    print("[%s]%s is a %s" % (title, name, gender_text))

print_info("Frank", "Teacher")
print_info("Rose", gender=False)


# the abbreviation should be in the end of the "def.."line
