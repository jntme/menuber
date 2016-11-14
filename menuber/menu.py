class Menu(object):
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

    def runMenupoint(self, menupointNumber):
        """Runs the Function on Menupoint with the given menupoint number (index + 1).
        """
        # TODO: this could be nicer ###############
        if not isinstance(menupointNumber, int):
            raise MenupointNotExistingError("Invalid input.")

        menupointNumber = menupointNumber - 1

        if menupointNumber < 0 or (menupointNumber + 1) > len(self.menupoints):
            raise MenupointNotExistingError("Invalid input.")
        ###########################################

        return self.menupoints[menupointNumber].runFunction()


class MenupointNotExistingError(Exception):
    def __init__(self, message):
        self.message = message
