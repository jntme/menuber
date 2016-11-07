
class Menuber:

    def __init__(self, menuTitle, menuFunctionMap):

        self.menuTitle = menuTitle
        self.menuFunctionMap = menuFunctionMap


    def menu(self):
        print(self.menuTitle)
        print(len(self.menuTitle)*"=")

        for entry in self.menuFunctionMap:
            print(entry, "\t", self.menuFunctionMap[entry])

    def callMenuPoint(self, menuPoint):
        if menuPoint not in self.menuFunctionMap:
            pass # RAISE ERROR!
        else:
            return self.menuFunctionMap[menuPoint]()
