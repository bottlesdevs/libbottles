from glob import glob
from bottle import Bottle
import globals


def list_bottles(paths: list):
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
        results += glob(p, recursive=True)

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
    list_bottles(
        paths=[f"{globals.Paths.bottles}*"]
    )[0].config["Parameters"]
)
'''


def list_runners():
    '''
    List local runners.

    Return
    ----------
    list:
        a list of Runner objects
    '''
    return


def list_dxvk():
    '''
    List local DXVK.

    Return
    ----------
    list:
        a list of DXVK objects
    '''
    return
