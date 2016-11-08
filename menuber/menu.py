class Menu:
    """
    Main class of the package. A menu contains menupoints.
    """
    def __init__(self, title, *menupoints):
        self.title = title
        self.menupoints = list(menupoints)

    def addMenupoint(self, menupoint):
        self.menupoints.append(menupoint)

    def addMenupoints(self, *menupoints):
        self.menupoints.extend(menupoints)

    def runMenupoint(self, menupointIndex):
        """Runs the Function on Menupoint with the given index."""
        print(self.menupoints[menupointIndex])
        return self.menupoints[menupointIndex].runFunction()

class MenupointNotExistingError(Exception):
    def __init__(self, message):
        self.message = message
