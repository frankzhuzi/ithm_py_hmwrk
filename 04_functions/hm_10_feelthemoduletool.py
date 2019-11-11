

def print_line(char, times):
    """print line

    :param char: the str you want to uses
    :param num: how many strings you want for a line
    """
    print(char * times)


def print_lines(char, times):
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1

name = "heima"