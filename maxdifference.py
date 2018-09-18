#!/usr/bin/python3

def maxDifference(a):

    max_difference = -1
    for i1 in range(len(a)):

        for i2 in range(i1):

            if a[i1] >= a[i2]:
                compare = a[i1] - a[i2]

                if compare > max_difference:
                    max_difference = compare

    return max_difference

if __name__ == '__main__':

    a = [6, 5, 10, 2, 1, 9, 1]

    print(maxDifference(a))




#def maxDifference(a):
#    max_value_index = 0
#    max_value = a[max_value_index]
#
#    for index in range(len(a)):
#        if a[index] > max_value:
#            max_value = a[index]
#            max_value_index = index
#
#max_difference = -1
#for index in range(len(a[:max_value_index])):
#    compare = max_value - a[index]
#    if compare > max_difference:
#        max_difference = compare
#return max_difference
