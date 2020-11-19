from unittest import TestCase
from roman_to_int import Solution


class Test(TestCase):
    def test_correct_input(self):
        self.assertTrue(Solution().correct_roman_str('MMMCMXCIX'))
        self.assertFalse(Solution().correct_roman_str('iilvd'))
        self.assertTrue(Solution().correct_roman_str(''))
        self.assertFalse(Solution().correct_roman_str('ABCDEFGHIJK'))

    def test_to_list(self):
        self.assertEqual(Solution().roman_to_int_list(''), [])
        self.assertEqual(Solution().roman_to_int_list('VV'), [5, 5])
        self.assertEqual(Solution().roman_to_int_list('LLL'), [50, 50, 50])
        self.assertEqual(Solution().roman_to_int_list('MMMM'), [1000, 1000, 1000, 1000])
        self.assertEqual(Solution().roman_to_int_list('DCXXIX'), [500, 100, 10, 10, 1, 10])
        self.assertEqual(Solution().roman_to_int_list('CMXCIX'), [100, 1000, 10, 100, 1, 10])

    def test_sub_principle(self):
        self.assertEqual(Solution().sub_principle([]), 0)
        self.assertEqual(Solution().sub_principle([500, 100, 10, 10, 1, 10]), 629)
        self.assertEqual(Solution().sub_principle([100, 1000, 10, 100, 1, 10]), 999)
        self.assertEqual(Solution().sub_principle([1000, 1000, 500, 100, 100, 50, 1, 5]), 2754)

    def test_main(self):
        self.assertEqual(Solution().roman_to_int(''), 0)
        self.assertEqual(Solution().roman_to_int('MMDCCLIV'), 2754)
        self.assertEqual(Solution().roman_to_int('MMDCCLIVMDXLSCC'),
                         'Count of input characters must be no more than 15')
        self.assertEqual(Solution().roman_to_int('MMDCCLIVXLS'),
                         'Input must be in Roman Numerals and follow proper syntax')
        self.assertNotEqual(Solution().roman_to_int('MMMMDXCVI'), 4596)




