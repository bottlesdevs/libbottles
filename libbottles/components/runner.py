from glob import glob
from random import seed, randint

from libwine.wine import Wine


class Runner:
    '''
    Create a new object of type Runner with all the methods for its management.

    Parameters
    ----------
    path : str
        the runner full path
    '''

    def __init__(self, path: str):
        self.__validate_runner(path)
    
    @staticmethod
    def __validate_runner(path: str):
        '''
        Check if essential paths exist in winepath.
        '''
        promise = ["lib64", "share", "bin", "lib"]

        dirs = glob(f"{path}/*")
        dirs = [d.replace(f"{path}/", "") for d in dirs]

        for p in promise:
            if p not in dirs:
                raise ValueError(
                    "Given path doesn't seem a valid Runner path.")

        return True