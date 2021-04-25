from glob import glob
from os import environ

from libwine.wine import Wine
from libwine.proton import Proton

from bottle import Bottle
from components.runner import Runner
import globals


class Manager:

    _bottles = []
    _components = []
    _environments = [
        "Software",
        "Gaming",
        "Custom"
    ]

    @staticmethod
    def update_bottles(paths: list = [globals.Paths.bottles]):
        '''
        Update user bottles.

        Parameters
        ----------
        paths : list
            paths to search for bottles
        '''
        results = []
        for p in paths:
            results += glob(f"{p}/*", recursive=True)
            
        for r in results:
            try:
                bottle = Bottle(r)
                Manager._bottles.append(bottle)
            except ValueError:
                continue

    @staticmethod
    def get_bottles():
        '''
        Get user bottles.

        Return
        ----------
        list:
            a list of Bottle objects
        '''
        return Manager._bottles

    @staticmethod
    def create_bottle(environment: int, path: str, name: str, runner: Runner, runner_path: str, versioning: bool, verbose: int):
        if not Manager._environments[environment]:
            raise ValueError(f"{environment} is not a valid environment.")
        
        config = {
            "Name": name,
            "Runner": runner_path,
            "Path": path,
            "Versioning": versioning,
            "Verbose": verbose
        }

        wineprefix = runner(
            winepath=runner_path,
            wineprefix=path
        )
        wineprefix.update()
        
        bottle = Bottle(path)
        bottle.apply_config(config)
        bottle.apply_environment(environment)

        Manager._bottles.append(bottle)
        return bottle


    # TODO: old code starts from here

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
