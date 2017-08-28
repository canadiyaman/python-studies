#!/usr/bin/env python3

import datetime


def year_area_control(date):
    if not date.year >= 1986 or not date.year <= 2050:
        raise IndexError


if __name__ == '__main__':
    while(True):

        try:

            date = datetime.datetime.strptime("%s" % (input("Given date format should be DD MM YYYY : ")), "%d %m %Y")

            year_area_control(date)

            previus_day = date - datetime.timedelta(1)

            print("%s" % previus_day.strftime('%d %m %Y'))



        except ValueError:
            print("You should give valid format date")
            continue

        except IndexError:
            print("Your given year must be between 1986 and 2050")
            continue



