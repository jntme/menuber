import unittest2 as unittest

from menuber.menupoint import Menupoint


def addThreeNumbers(a, b, c):
    return a + b + c


def subtractOneNumberFromAnother(a, b):
    return a - b


class TestMenupoint(unittest.TestCase):
    def setUp(self):
        arguments = [2, 8, 10]
        self.testMenuPoint1 = Menupoint("addThreeNumbers", addThreeNumbers, *arguments)
        self.testMenuPoint2 = Menupoint("subtractOneNumberFromAnother", subtractOneNumberFromAnother, 10, 5)

    def testRunFunction(self):
        self.assertEqual(self.testMenuPoint1.runFunction(), 20)
        self.assertEqual(self.testMenuPoint2.runFunction(), 5)
