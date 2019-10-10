import unittest


class Check(unittest.TestCase):

    def __init__(self):
        self.flag = 0
        self._type_equality_funcs = {}

    def equal(self, a, e, m):
        try:
            self.assertEqual(a, e, m)
        except Exception as e:
            print(m)
            print(e)
            self.flag += 1

    def notEqual(self, a, e, m):
        try:
            self.assertNotEqual(a, e, m)
        except:
            print(m)
            self.flag += 1

    def gt(self, a, e, m):
        try:
            self.assertEqual(a > e, True, m)
        except:
            print(m)
            self.flag += 1

    def notNone(self, a, e, m):
        try:
            self.assertIsNotNone(a, e, m)
        except:
            print(m)
            self.flag += 1

    def notIn(self, a, e, m):
        try:
            self.assertNotIn(a, e, m)
        except:
            print(m)
            self.flag += 1

    def result(self, message):
        if self.flag > 0 :
            self.assertTrue(False)
        else:
            self.assertTrue(True)
            print(message)

    def false(self, message):
        try:
            self.assertTrue(False, message)
        except:
            print(message)
            self.flag += 1