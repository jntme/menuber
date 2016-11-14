
class Menupoint(object):
    """A menupoint is one possible selection in the cli menu.
    It takes a name, a function to call the eventual arguments for the fucntion
    as arguments."""

    def __init__(self, name, function, *args):
        self.name = name
        self.function = function
        self.args = list(args)

    def runFunction(self):
        return self.function(*self.args)
