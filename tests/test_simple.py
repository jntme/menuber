import unittest2 as unittest

from menuber import Menuber

#test functions
#######################################
def testFunc1():
    return 1337;

def testFunc2(a, b):
    return a + b
#######################################

class TestMenuber(unittest.TestCase):
    def test_newMenuberNaming(self):
        new_menu = Menuber.Menuber("Testname", {1: "Test1", 2: "Test2"})

        self.assertEqual(new_menu.menuTitle, "Testname")
        self.assertEqual(new_menu.menuFunctionMap[1], "Test1")

    def test_printMenu(self):
        new_menu = Menuber.Menuber("Testname", {1: testFunc1, 2: testFunc2(1,2)})

        new_menu.menu()

    def test_newMenuberFunctionCalling(self):
        new_menu = Menuber.Menuber("Testname", {1: testFunc1})

        self.assertEqual(new_menu.callMenuPoint(1), 1337);
