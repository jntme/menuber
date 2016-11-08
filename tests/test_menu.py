import unittest2 as unittest

import menuber


def addThreeNumbers(a, b, c):
    return a + b + c


def subtractOneNumberFromAnother(a, b):
    return a - b


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.testMenu = menuber.Menu("TestMenu")
        menuPoint1 = menuber.Menupoint("Menupoint1", addThreeNumbers, 1, 2, 3)  # = 6
        menuPoint2 = menuber.Menupoint("Menupoint2", subtractOneNumberFromAnother, 15, 20)  # = -5

        self.testMenu.addMenupoints(menuPoint1, menuPoint2)

    def testWhatWhenNoMenuInsertedOnInit(self):
        testMenu = menuber.Menu("TestMenu")
        self.assertEqual(len(testMenu.menupoints), 0)
        menuPoint1 = menuber.Menupoint("Menupoint1", addThreeNumbers, 1, 2, 3)  # = 6

        testMenu.addMenupoint(menuPoint1)
        self.assertEqual(len(testMenu.menupoints), 1)

    def testAreMenuPointsExisting(self):
        self.assertEqual(len(self.testMenu.menupoints), 2)

    def testRunFirstFunction(self):
       self.assertEqual(self.testMenu.runMenuPoint(1), 6)

    def testRunSecondFunction(self):
        pass

