from glob import glob
from libbottles.utils.request import Request
from libbottles import globals


class Repository:
    
    _index = []

    def __init__(self):
        self.update_index()
    
    def update_index(self):
        r = Request()
        self._index = r.get(globals.Repository.components_index)


Repository()