def square(the_list):
    return [x*x for x in the_list]

def merge(x, y):
    if len(x) == 0:
        return y
    elif len(y) == 0:
        return x

    elif x[-1] <= y[0]:
        return [x[-1]] + merge(x[:-1], y)
    else:
        return [y[0]] + merge(x, y[1:])


the_list = [-8, -5, -3, -1, 4, 7, 12, 24]
half_the_list = int(len(the_list)/2)
list1 = square(the_list[:half_the_list])
list2 = square(the_list[half_the_list:])

print(merge(list1, list2))

