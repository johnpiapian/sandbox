from Engine import *
from IO import *
from Subject import *


def enum_names(enum_class):
    return [member.name for member in enum_class]


def option_wrapper(options: List):
    options.insert(0, str('Move'))
    return options


def app():
    fox = Subject(SubjectType.FARMER, [SubjectType.CHICKEN])
    chicken = Subject(SubjectType.CHICKEN, [SubjectType.GRAIN])
    grain = Subject(SubjectType.GRAIN)

    actors = [fox, chicken, grain]

    game = Engine(actors)

    while not game.ended():

        stats = (game.farmer_location, game.get_north(), game.get_south())
        IO.displayStatus(stats)

        # selectable_actors = game.get_selectable_actors()
        # options = option_wrapper(enum_names(selectable_actors))
        #
        # user_response = IO.showMenu(options, 'Select actor to bring: ')
        #
        # if user_response == 0:  # move
        #     IO.cross_the_river()
        # else:
        #     # keep asking
        #     pass


app()
