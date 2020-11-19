# python3.6
# coding: utf-8

import re


class Solution:

    def correct_roman_str(self, s):
        """
        Checks string for letters that are Roman Numerals and follow the rules.
        Returns False if string isn't correct Roman Numeral.
        """
        regex = re.compile(r"^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$")
        return regex.match(s)

    def roman_to_int_list(self, s):
        """
        Converts Roman Numerals to a list of numbers.
        """
        converters = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        list_of_numbers = []

        for numeral in s:
            for key in converters:
                if numeral == key:
                    list_of_numbers.append(converters[key])
        return list_of_numbers

    def sub_principle(self, list_of_num):
        """
        Subtractive Principle
        If a smaller number occurs before a larger number, the former is subtracted.
        - e.g.(XC ==> C - X ==> 100 - 10 = 90).
        """
        result = 0
        for index in range(len(list_of_num) - 1):
            if list_of_num[index] < list_of_num[index + 1]:
                list_of_num[index + 1] -= list_of_num[index]
                list_of_num[index] = 0
        for numbers in list_of_num:
            result += numbers
        return result

    def roman_to_int(self, s):
        """
        Main function.
        Takes a string format.
        Checks for all conditions for a valid Roman Numeral.
        Return int if all conditions are correct.
        Return an error message if one of the condition isn't passed.
        """
        # user input length mustn't be more than 15 characters
        if len(s) >= 15:
            output = 'Count of input characters must be no more than 15'

        # user input must be a string that consists Roman Numeral letters and follow proper syntax
        elif s.isdigit() or not self.correct_roman_str(s):
            output = 'Input must be in Roman Numerals and follow proper syntax'

        # numbers equal to 4000 and up require a special character and can't be handled
        elif self.sub_principle(self.roman_to_int_list(s)) >= 4000:
            output = "Sorry. Can't handle numbers 4000 or greater."

        else:
            output = self.sub_principle(self.roman_to_int_list(s))
        return output


if __name__ == '__main__':
    roman_input = input()
    result = Solution().roman_to_int(roman_input)
    print(f'{roman_input} --> {result}')
