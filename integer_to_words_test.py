#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
import integer_to_words


class ToWordsTests(unittest.TestCase):
    def setUp(self):
        self.cut = integer_to_words.IntegerToWordsConverter()  # (C)lass (U)nder (T)est

    def test_that_single_digits_return_words(self):
        test_cases = [(1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"), (6, "six"), (7, "seven"),
                      (8, "eight"), (9, "nine")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_that_non_teen_two_digits_returns_words(self):
        test_cases = [(10, "ten"), (11, "eleven"), (12, "twelve")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_that_unique_teens_return_words(self):
        test_cases = [(13, "thirteen"), (15, "fifteen"), (18, "eighteen")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_that_simple_teens_return_words(self):
        test_cases = [(14, "fourteen"), (16, "sixteen"), (17, "seventeen"), (19, "nineteen")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_even_tens(self):
        test_cases = [(10, "ten"), (20, "twenty"), (30, "thirty"), (40, "forty"), (50, "fifty"), (60, "sixty"),
                      (70, "seventy"), (80, "eighty"), (90, "ninety")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_two_digit_hyphens(self):
        test_cases = [(21, "twenty-one"), (22, "twenty-two"), (39, "thirty-nine"), (45, "forty-five"),
                      (53, "fifty-three"), (66, "sixty-six"), (78, "seventy-eight"), (87, "eighty-seven"),
                      (98, "ninety-eight"), (99, "ninety-nine")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_hundreds(self):
        test_cases = [(100, "one hundred"), (101, "one hundred one"), (110, "one hundred ten"),
                      (253, "two hundred fifty-three"), (999, "nine hundred ninety-nine")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_thousands(self):
        test_cases = [(1000, "one thousand"), (1001, "one thousand one"),
                      (1999, "one thousand nine hundred ninety-nine"),
                      (10000, "ten thousand"), (10001, "ten thousand one"),
                      (23142, "twenty-three thousand one hundred forty-two"),
                      (19999, "nineteen thousand nine hundred ninety-nine"),
                      (99999, "ninety-nine thousand nine hundred ninety-nine"),
                      (745111, "seven hundred forty-five thousand one hundred eleven")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_millions(self):
        test_cases = [(1000000, "one million"),
                      (987654321, "nine hundred eighty-seven million "
                                  "six hundred fifty-four thousand "
                                  "three hundred twenty-one")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_billions(self):
        test_cases = [(1000000000, "one billion"),
                      (789123234001, "seven hundred eighty-nine billion "
                                     "one hundred twenty-three million "
                                     "two hundred thirty-four thousand "
                                     "one")]
        for n, expected in test_cases:
            self.assertEqual(expected, self.cut.to_words(n))

    def test_all_place_names(self):
        p = 1
        n = 0
        for _ in self.cut.place_names:
            p *= 1000
            n += p
        n += 116
        self.assertEqual("one duotrigintillion one untrigintillion one trigintillion one novemvigintillion "
                         "one octovigintillion one septenvigintillion one sexvigintillion one quinvigintillion "
                         "one quattuorvigintillion one trevigintillion one duovigintillion one unvigintillion "
                         "one vigintillion one novemdecillion one octodecillion one septendecillion one sexdecillion "
                         "one quindecillion one quattuordecillion one tredecillion one duodecillion one undecillion "
                         "one decillion one nonillion one octillion one septillion one sextillion one quintillion "
                         "one quadrillion one trillion one billion "
                         "one million one thousand one hundred sixteen", self.cut.to_words(n))

    def test_unknown_value(self):
        max_limit = 10 ** 102
        self.assertEqual("unknown", self.cut.to_words(max_limit))

    def test_zero(self):
        self.assertEqual("zero", self.cut.to_words(0))


if __name__ == '__main__':
    unittest.main()
