from glob import glob
from bottle import Bottle
from components.runner import Runner
import globals


def list_bottles(paths: list = [globals.Paths.bottles]):
    '''
    List user bottles.

    Parameters
    ----------
    paths : list
        paths to search for bottles

    Return
    ----------
    list:
        a list of Bottle objects
    '''
    results = []
    for p in paths:
        results += glob(f"{p}/*", recursive=True)

    bottles = []
    for r in results:
        try:
            bottle = Bottle(r)
            bottles.append(bottle)
        except ValueError:
            continue

    return bottles


'''
print(
    list_bottles()[0].config["Parameters"]
)
'''


def list_runners(paths: list = [globals.Paths.runners]):
    '''
    List local runners.

    Return
    ----------
    list:
        a list of Runner objects
    '''
    results = []
    for p in paths:
        results += glob(f"{p}/*", recursive=True)

    runners = []
    for r in results:
        try:
            runner = Runner(r)
            runners.append(runner)
        except ValueError:
            continue

    return runners


print(
    list_runners()
)


def list_dxvk():
    '''
    List local DXVK.

    Return
    ----------
    list:
        a list of DXVK objects
    '''
    return
