import unittest
import balmedadv_locators as locators
import balmedadv_methods as methods

class BalleMediaAdvPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_main_balle_media_adv():
        methods.setUp()
        methods.grow_your_clinic()
        methods.page_one()
        methods.page_two()
        methods.page_three()
        methods.page_four()
        methods.page_five()
        methods.tearDown()