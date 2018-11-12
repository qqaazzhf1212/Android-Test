import unittest
from ddt import unpack,ddt,data

@ddt
class MyTestCase(unittest.TestCase):

    @data(1,2,2,3)
    def test_something(self,value):
        print(value)
        self.assertEqual(value, 2)

    @data((1,2),(2,3))
    @unpack
    def test_something1(self,value1,value2):
        print(value1,value2)
        self.assertEqual(value2, value1+value2)

if __name__ == '__main__':
    unittest.main()
