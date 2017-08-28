#!/usr/bin/env python3


class rectangle():

    def __init__(self):
        # s is short edge
        self.s = 1
        # l is long edge
        self.l = 2

    def get_area(self):
        # Calculating rectangle area
        return self.s * self.l

    def edge_control(self):
        if self.l > self.s:
            return True
        return False

def checked(Z, s,l):

    if (2 * l) + (2 * s) <= Z and s > 0:
        return True
    return False


if __name__ == '__main__':
    try:
        Z = int(input("The first line contains single integer Z -"))

        rectangle = rectangle()
        # posibilities will take list of posibilities of rentacgle areas
        posibilities = []

        while (checked(Z, rectangle.s, rectangle.l)):

            area = rectangle.get_area()
            if rectangle.edge_control():
                posibilities.append(area)

            rectangle.l = rectangle.l + 1
            rectangle.s = int((Z - rectangle.l * 2) / 2)
            # int((Z - (rectangle.s * 2)) / 2)

        posibilities.sort()
        print("The largest renctacle that can be formed using the given straws: %d " % posibilities[-1])

    except ValueError:
        print("You should give integer number !")

    except IndexError:
        print("Nothing Found")




