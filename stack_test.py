import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
    
    def test_2(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(3)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertTrue(stack.is_full())
    
    def test_3(self):
        stack = Stack(4)
        self.assertTrue(stack.is_empty())
    
    def test_4(self):
        stack = Stack(2)
        stack.push(0)
        stack.push(1)
        with self.assertRaises(IndexError):
            stack.push(2)

    def test_5(self):
        stack = Stack(2)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_6(self):
        stack = Stack(2)
        with self.assertRaises(IndexError):
            stack.peek()

    def test_7(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)
            
if __name__ == '__main__': 
    unittest.main()
