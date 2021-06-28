class Component:
    """
    Create a new object of type Component with all the methods for its management.

    Parameters
    ----------
    manifest : dict
        the component manifest
    local : bool
        if this is a local (installed) component (default is False)
    """

    manifest = {}
    _manifest_struct = {
        "Name": "",
        "Provider": "",
        "Channel": ""
    }

    def __init__(self, manifest: dict, local: bool = False):
        self.manifest = manifest
        if not self.__validate():
            raise ValueError("Given manifest doesn't seem a valid Component.")

        self.installed = local

    def __validate(self):
        """
        Check if essential keys exist in manifest.
        """
        if all(key in self.manifest for key in self._manifest_struct.keys()):
            return True
        return False
