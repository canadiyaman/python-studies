#!/usr/bin/env python3



#A palindrome is a word that reads the same backward or forward.
#Write a function that checks if a given word is a palindrome. Character case should be ignored.
#For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.




class Palindrome:

    @staticmethod
    def is_palindrome(word):
        if str.lower(word) == str.lower(word[::-1]):
            return True
        return False

    @staticmethod
    def is_palindrome2(word):
        p_word = ""
        for w in word:
            p_word += w

        if str.lower(word) == str.lower(p_word):
            return True
        return False

if __name__ == '__main__':
    word = input("Give me a word and i checked is palindrome: ")
    print(Palindrome.is_palindrome2(word))
