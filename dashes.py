#!/usr/bin/env python3


# Each digit is made of a certain number  of dashes, as shown in the image below.
# or example 1 is made of 2 dashes, 8 is made of 7 dashes and so on

class Dashes():

    def __init__(self):
        self.numbers = None
        self.digits = {
            "0" : 6,
            "1" : 2,
            "2" : 5,
            "3" : 5,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 4,
            "8" : 7,
            "9" : 6
        }

    def get_digit_count(self):
        count = 0
        for number in list(self.numbers):
            count += self.digits[number]
        return count



if __name__ == '__main__':

    dashes = Dashes()
    dashes.numbers = str(input("Give me some number: "))
    print(dashes.get_digit_count())
