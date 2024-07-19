import unittest
from is_prime import is_prime

class TryTesting(unittest.TestCase):
    def test_regular_prime(self):
        self.assertTrue(is_prime(7))
    
    def test_regular_prime_large(self):
        self.assertTrue(is_prime(113))
    
    def test_regular_nonprime(self):
        self.assertFalse(is_prime(12))
    
    def test_edge(self):
        self.assertFalse(is_prime(1))
    
    def test_edge2(self):
        self.assertFalse(is_prime(0))

    def test_edge_negative(self):
        self.assertFalse(is_prime(-20))

    def test_always_passes(self):
        self.assertTrue(True)
    
    def test_always_fails(self):
        self.assertFalse(False)

if __name__ == "__main__":
    unittest.main()
