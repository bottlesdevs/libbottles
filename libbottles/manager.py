from glob import glob

from libbottles.bottle import Bottle
from libbottles.components.runner import Runner
from libbottles import globals


class Manager:
    _bottles = []
    _runners = []
    _dxvks = []

    @staticmethod
    def update_bottles(paths: list = None):
        """
        Update user bottles.

        Parameters
        ----------
        paths : list
            paths to search for bottles
        """
        Manager._bottles = []
        results = []
        if paths is None:
            paths = [globals.Paths.bottles]

        for p in paths:
            results += glob(f"{p}/*", recursive=True)

        for r in results:
            bottle = Bottle(r)
            Manager._bottles.append(bottle)
            try:
                bottle = Bottle(r)
                Manager._bottles.append(bottle)
            except ValueError:
                continue

    @staticmethod
    def update_runners(paths=None):
        """
        Update local runners.

        Parameters
        ----------
        paths : list
            paths to search for runners
        """
        Manager._runners = []
        results = []
        if paths is None:
            paths = [globals.Paths.runners]

        for p in paths:
            results += glob(f"{p}/*", recursive=True)

        for r in results:
            try:
                runner = Runner(r)
                Manager._runners.append(runner)
            except ValueError:
                continue

    @staticmethod
    def get_bottles():
        """
        Get user bottles.

        Return
        ----------
        list:
            a list of Bottle objects
        """
        return Manager._bottles

    @staticmethod
    def get_runners():
        """
        Get local runners.

        Return
        ----------
        list:
            a list of Runner objects
        """
        return Manager._runners

    @staticmethod
    def get_dxvks():
        """
        Get local dxvks.

        Return
        ----------
        list:
            a list of Dxvk objects
        """
        return Manager._dxvks

    @staticmethod
    def create_bottle(
            path: str,
            env: int,
            name: str,
            runner_path: str,
            versioning: bool = False,
            verbose: int = 0):

        bottle = Bottle(
            path=path,
            create=True,
            env=env,
            name=name,
            runner_path=runner_path,
            versioning=versioning,
            verbose=verbose
        )

        Manager._bottles.append(bottle)
        return bottle
