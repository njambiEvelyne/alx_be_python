import unittest
"""""
Function to test
"""
def add(x,y):
  return x+y

def mult(a,b):
  return a*b

def subtr(a,b):
  return (a - b)

class TestOperation(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(6,7), 13)
    self.assertEqual(mult(2,4), 8)
    self.assertEqual(subtr(1,4), 8)



unittest.main()
