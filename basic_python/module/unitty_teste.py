## create tests to verify the correct functions operation
import unittest

#My functions
import my_math


class Teste_My_Math( unittest.TestCase):
    def test_fib(self):
        self.assertEqual(832040, my_math.fib_(30))

    def teste_pow(self):
        self.assertEqual(100, my_math.pow_(10,2))
    
    def teste_fat(self):
        self.assertEqual(3628800, my_math.fat_(15))


unittest.main()
