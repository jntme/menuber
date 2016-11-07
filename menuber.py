
class Menuber:

    def __init__(self, menuTitle, menuFunctionMap, subMenu=None):

        self.menuTitle = menuTitle
        self.menuFunctionMap = menuFunctionMap


    def menu(self):
        print(self.menuTitle)
        print(len(self.menuTitle)*"=")
        print("")

        for entry in self.menuFunctionMap:
            print(entry, "\t", self.menuFunctionMap[entry])

        #user_input = input(">> ")

        #print(user_input)

    def callMenuPoint(self, menuPoint):
        if menuPoint not in self.menuFunctionMap:
            raise MenuPointNotExistingError("No such menu point in map!")
        else:
            return self.menuFunctionMap[menuPoint]()

class Error(Exception):
    '''Base class for exceptions in this module.'''
    pass

class MenuPointNotExistingError(Error):

    def __init__(self, message):
        self.message = message