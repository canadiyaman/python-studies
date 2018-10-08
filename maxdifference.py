#!/usr/bin/python3


# Given array has some integers. 
# We are trying to find max difference between an integer in array and situated in array more lower index integers.


def maxDifference(a):

    max_difference = -1
    for i1 in range(len(a)):

        for i2 in range(i1):

            if a[i1] >= a[i2]:
                difference = a[i1] - a[i2]

                if difference > max_difference:
                    max_difference = difference

    return max_difference

if __name__ == '__main__':

    a = [6, 5, 10, 2, 1, 9, 1]

    print(maxDifference(a)) # => 8 Result is 8 because for this example, max difference between 9 - 1 = 8.
