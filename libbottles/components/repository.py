from glob import glob
from libbottles.utils.request import Request
from libbottles import globals


class Repository:
    
    _index = []

    def __init__(self):
        self.update_index()
    
    def update_index(self):
        r = Request()
        # TODO: paths should be defined in globals
        self._index = r.get("https://raw.githubusercontent.com/bottlesdevs/components/main/index.json")
        print(self._index)


Repository()