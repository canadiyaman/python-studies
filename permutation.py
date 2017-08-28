#!/usr/bin/env python3

class Permutation:

    def __init__(self):
        self.key = ""
        self.pattern = ""

    def is_checked(self):
        pattern_list = list(self.pattern)
        for word in self.key:
            if not word in pattern_list:
                return "NO"
            pattern_list.remove(word)
        return "YES"




if __name__ == '__main__':

    permutation = Permutation()
    permutation.key = input("Key: ")
    permutation.pattern = input("Pattern: ")
    print(permutation.is_checked())
