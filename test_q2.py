import unittest
from q2 import find_article_references


class TestQuestion2(unittest.TestCase):

    def set_up_base_case(self):
        self.base_case = {
            123: [458, 812, 765],
            458: [123, 812, 765],
            812: [123, 458],
            765: [123, 458],
            999: [100],
            100: [999]
        }
        self.base_case_expected = {
            (123, 458), (123, 812), (123, 765), (458, 812), (458, 765), (100, 999)
        }

    def set_up_empty_case(self):
        self.empty_case = {

        }

    def test_base_case(self):
        self.set_up_base_case()
        self.assertGreater(len(self.base_case), 0)
        r = find_article_references(self.base_case)
        self.assertEquals(r, self.base_case_expected)

    def test_empty_case(self):
        self.set_up_empty_case()
        self.assertEquals(len(self.empty_case), 0)
        r = find_article_references(self.empty_case)
        self.assertEquals(r, None)

