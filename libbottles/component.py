class Component:
    '''
    Create a new object of type Component with all the methods for its management.

    Parameters
    ----------
    manifest : dict
        the component manifest
    local : bool
        if this is a local (installed) component (default is False)
    '''

    name = str
    category = str
    sub_category = str
    channel = str
    manifest_url = str
    installed = False

    def __init__(self, manifest: dict, local: bool = False):
        if not self.validate_manifest(manifest):
            raise ValueError("Given manifest doesn't seem a valid Component.")
            
        self.installed = local

    def validate_manifest(self, manifest: dict):
        return
