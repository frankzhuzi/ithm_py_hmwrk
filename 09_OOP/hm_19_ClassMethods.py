class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):

        print("We have %d tools" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1




Tool.show_tool_count()