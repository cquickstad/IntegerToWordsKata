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


class IntegerToWords:
    # translations is a dictionary that handles basic cases (i.e. 2=>'two')
    # and cases which must map because they are special (i.e. 13=>'thirteen' not 'threeteen').
    # This dictionary is the base of higher recursive calls that handle the billions, thousands, etc.
    # (i.e. the 'three' in 'three billion').
    translations = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
                    8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                    15: "fifteen", 18: "eighteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

    NAME = 0
    VALUE = 1
    LIMIT = 2
    place_name_value_limit = [
        ("thousand",
         1_000,
         999_999),
        ("million",
         1_000_000,
         999_999_999),
        ("billion",
         1_000_000_000,
         999_999_999_999),
        ("trillion",
         1_000_000_000_000,
         999_999_999_999_999),
        ("quadrillion",
         1_000_000_000_000_000,
         999_999_999_999_999_999),
        ("quintillion",
         1_000_000_000_000_000_000,
         999_999_999_999_999_999_999),
        ("sextillion",
         1_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999),
        ("septillion",
         1_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999),
        ("octillion",
         1_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999),
        ("nonillion",
         1_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999),
        ("decillion",
         1_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999),
        ("undecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("duodecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("tredecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("quattuordecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("quindecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("sexdecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("septendecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("octodecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("novemdecillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("vigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("unvigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("duovigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("trevigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("quattuorvigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("quinvigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("sexvigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("septenvigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("octovigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("novemvigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("trigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("untrigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999),
        ("duotrigintillion",
         1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000,
         999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999_999)]

    @staticmethod
    def compound_teen_to_words(n):
        ones_digit = n - 10
        return IntegerToWords.translations[ones_digit] + "teen"

    @staticmethod
    def two_digit_hyphen_to_words(n):
        tens_value = int(n / 10) * 10
        ones_value = n - tens_value
        return IntegerToWords.translations[tens_value] + "-" + IntegerToWords.translations[ones_value]

    @staticmethod
    def recursive_conversion_starting_at_place(n, place_name, place_value):
        value_in_place = int(n / place_value)
        integer_remainder = n - (value_in_place * place_value)
        remainder_in_words = (" " + IntegerToWords.to_words(integer_remainder)) if integer_remainder > 0 else ""
        return IntegerToWords.to_words(value_in_place) + " " + place_name + remainder_in_words

    @staticmethod
    def hundreds_to_words(n):
        return IntegerToWords.recursive_conversion_starting_at_place(n, "hundred", 100)

    @staticmethod
    def get_largest_place_name_and_value(n):
        for name, value, limit in IntegerToWords.place_name_value_limit:
            if n < limit:
                return name, value

    @staticmethod
    def large_number_to_words(n):
        place_name, place_value = IntegerToWords.get_largest_place_name_and_value(n)
        return IntegerToWords.recursive_conversion_starting_at_place(n, place_name, place_value)

    @staticmethod
    def to_words(n):
        if n in IntegerToWords.translations:
            return IntegerToWords.translations[n]
        elif n < 20:
            return IntegerToWords.compound_teen_to_words(n)
        elif n < 100:
            return IntegerToWords.two_digit_hyphen_to_words(n)
        elif n < 1000:
            return IntegerToWords.hundreds_to_words(n)
        elif n < IntegerToWords.place_name_value_limit[-1][IntegerToWords.LIMIT]:
            return IntegerToWords.large_number_to_words(n)
        else:
            return "unknown"


def parse_arguments():
    ap = ArgumentParser(description="Integer to Words")
    ap.add_argument('integer', nargs='?', type=int, default=None, help="Integer to convert to words")
    return ap.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if args.integer is None:
        args.integer = int(sys.stdin.read())
    print(IntegerToWords.to_words(args.integer))
