from glob import glob
from bottle import Bottle


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
        paths=["/home/mirko/.local/share/bottles/bottles/*"]
    )
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
