from typing import Tuple


class IO:
    def __init__(self):
        pass

    @staticmethod
    def askInput(msg='', type2be=str):
        while True:
            user_input = input(msg)
            try:
                # Try to convert user input to the specified type
                user_input = type2be(user_input)
                return user_input
            except ValueError:
                # If conversion fails, ask for input again
                print('Invalid Input! Please type again.')

    @staticmethod
    def showMenu(options=[], msg=''):
        print("Select an option:")

        for index, item in enumerate(options):
            print('{0}) {1}'.format(index, item))

        return IO.askInput(msg, int)

    @staticmethod
    def displayStatus(stats: Tuple):
        farmer_location, north, south = stats

        result = ""
        for name in north:
            result += " {0} ".format(name)

        if farmer_location == 0:
            result += " * "

        result += "\n"
        for i in range(0, max(len(north), len(south)) * 5):
            result += " _ "

        result += "\n"
        for name in south:
            result += " {0} ".format(name)

        if farmer_location == 1:
            result += " * "

