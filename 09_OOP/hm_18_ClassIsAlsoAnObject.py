class Tool(object):

    count = 0
    # Class Tool's Nature

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("Axe")
tool2 = Tool("Bucket")

print(Tool.count)
print(tool1.count)
# Search a Nature upwards
# Found no Tool.count in __init, so search class Tool
