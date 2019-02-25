#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Integer To Words
#
# http://codingdojo.org/kata/NumbersInWords/
#
# Convert integer value to word equivalent similar to how you would write out the number on a check.
#
# FYI:
#
#       Review english grammar:
#           http://www.grammarbook.com/numbers/numbers.asp
#
#       Review large number names:
#           http://bmanolov.free.fr/numbers_names.php
from argparse import ArgumentParser
import sys


class IntegerToWordsConverter:
    def __init__(self):
        # translations is a dictionary that handles basic cases (i.e. 2=>'two')
        # and cases which must map because they are special (i.e. 13=>'thirteen' not 'threeteen').
        # This dictionary is the base of higher recursive calls that handle the billions, thousands, etc.
        # (i.e. the 'three' in 'three billion').
        self.translations = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
                             8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                             15: "fifteen", 18: "eighteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                             60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

        # Assumption: place names in this list are separated by a factor of 1000 in increasing order
        self.place_names = ["thousand", "million", "billion", "trillion", "quadrillion",
                            "quintillion", "sextillion", "septillion", "octillion",
                            "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion",
                            "quattuordecillion", "quindecillion", "sexdecillion", "septendecillion",
                            "octodecillion", "novemdecillion", "vigintillion", "unvigintillion",
                            "duovigintillion", "trevigintillion", "quattuorvigintillion",
                            "quinvigintillion", "sexvigintillion", "septenvigintillion",
                            "octovigintillion", "novemvigintillion", "trigintillion",
                            "untrigintillion", "duotrigintillion"]

        self.max_limit = self.get_place_value(len(self.place_names))

    @staticmethod
    def div_round_down(n, denominator):
        return int(n / denominator)

    @staticmethod
    def get_place_value(place_names_index):
        zero_index_offset = 1
        thousand_exponent = 3
        return 10 ** ((place_names_index + zero_index_offset) * thousand_exponent)

    def compound_teen_to_words(self, n):
        ones_digit = n - 10
        return self.translations[ones_digit] + "teen"

    def two_digit_hyphen_to_words(self, n):
        tens_value = IntegerToWordsConverter.div_round_down(n, 10) * 10
        ones_value = n - tens_value
        return self.translations[tens_value] + "-" + self.translations[ones_value]

    def recursive_conversion_starting_at_place(self, n, place_name, place_value):
        value_in_place = IntegerToWordsConverter.div_round_down(n, place_value)
        integer_remainder = n - (value_in_place * place_value)
        remainder_in_words = (" " + self.to_words(integer_remainder)) if integer_remainder > 0 else ""
        return self.to_words(value_in_place) + " " + place_name + remainder_in_words

    def hundreds_to_words(self, n):
        return self.recursive_conversion_starting_at_place(n, "hundred", 100)

    def get_largest_place_name_and_value(self, n):
        for i, place_name in enumerate(self.place_names):
            place_limit = self.get_place_value(i + 1)
            if n < place_limit:
                return place_name, self.get_place_value(i)

    def large_number_to_words(self, n):
        place_name, place_value = self.get_largest_place_name_and_value(n)
        return self.recursive_conversion_starting_at_place(n, place_name, place_value)

    def to_words(self, n):
        if n in self.translations:
            return self.translations[n]
        elif n < 20:
            return self.compound_teen_to_words(n)
        elif n < 100:
            return self.two_digit_hyphen_to_words(n)
        elif n < 1000:
            return self.hundreds_to_words(n)
        elif n < self.max_limit:
            return self.large_number_to_words(n)
        else:
            return "unknown"


def parse_arguments():
    ap = ArgumentParser(description="Integer to Words")
    ap.add_argument('integer', nargs='?', type=int, default=None, help="Integer to convert to words")
    return ap.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    converter = IntegerToWordsConverter()
    if args.integer is None:
        args.integer = int(sys.stdin.read())
    print(converter.to_words(args.integer))
