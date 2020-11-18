# python3.6
# coding: utf-8

import re


class Solution:

    def roman_to_int(self, s):
        """
        Make integer number from Roman Numeral
        """
        list_of_num = self.roman_to_int_list(s)
        return self.sub_principle(list_of_num)

    def match_roman_str(self, s):
        """
        Checks string for letters that are Roman Numerals.
        Returns False if string contains foreign characters.
        """
        regex = re.compile(r"(?i)^[IVXLCDM]+$")
        return regex.match(s)

    def power_of_ten(self, s):
        return s == 1 or s % 10 == 0

    def valid_roman(self, s):
        """
        Checks string for valid Roman Numerals syntax.
        """
        numbers = self.roman_to_int_list(s)
        for index in range(len(numbers) - 1):
            next_num = numbers[index + 1]
            if numbers[index] == next_num:
                return True
            elif numbers[index] * 10 >= next_num:
                return self.power_of_ten(numbers[index])

    def roman_to_int_list(self, s):
        """
        Converts Roman Numerals to a list of numbers.
        """
        converters = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        numbers = []
        for numeral in s:
            for key in converters:
                if numeral == key:
                    numbers.append(converters[key])
        return numbers

    def sub_principle(self, list_of_num):
        """
        Subtractive Principle
        If a smaller number occurs before a larger number, the former is subtracted.
        - e.g.(XC ==> C - X ==> 100 - 10 = 90)
        """
        result = 0
        for index in range(len(list_of_num) - 1):
            if list_of_num[index] < list_of_num[index + 1]:
                list_of_num[index + 1] -= list_of_num[index]
                list_of_num[index] = 0
        for numbers in list_of_num:
            result += numbers
        return result

    def repetition_rule(self, s):
        """
        Checks for a Numeral that repeats consecutively four times or more
        """
        freq = []
        for index in range(len(s) - 1):
            if s[index] == s[index + 1]:
                if freq:
                    freq.append(s[index])
                else:
                    freq.append(s[index])
                    freq.append(s[index + 1])
            else:
                freq.clear()
        return len(freq) >= 4

    def count(self, s):
        """
        Main function.
        Takes string format.
        Checks for all conditions for a valid Roman Numeral.
        Return int if all conditions are correct.
        Return an error message if one of the condition isn't passed
        """
        # user input length mustn't be more than 15 characters
        if len(s) >= 15:
            output = 'Count of input characters must be no more than 15'

        # user input must be a string that consists Roman Numeral letters
        elif s.isdigit() or not self.match_roman_str(s):
            output = 'Input must be in Roman Numerals'

        # user input must follow proper syntax
        elif not self.valid_roman(s):
            output = ("Your syntax is wrong. Follow these rules:\n"
                      "Only 'I' can go before 'V' or 'X',\n"
                      "'X' before 'L' or 'C',\n"
                      "'C' before 'D' or 'M'.")

        # numbers equal to 4000 and up require a special character and can't be handled
        elif self.sub_principle(self.roman_to_int_list(s)) >= 4000:
            output = "Sorry. Can't handle numbers 4000 or greater."

        # user input cannot have a Roman Numeral that repeats four times or more in row
        elif self.repetition_rule(s):
            output = 'Is your key stuck?'
        else:
            output = f'{s} --> {self.roman_to_int(s)}'
        return output


if __name__ == '__main__':
    roman_input = input()
    res = Solution().count(roman_input)
    print(res)
