import json
from glob import glob
from random import seed, randint
seed(1)


class Bottle:
    '''
    Create a new object of type Bottle with all the methods for its management.

    Parameters
    ----------
    path : str
        the bottle full path
    '''
    name = str
    path = str
    runner = str
    dxvk = str
    environment = int
    creation_date = str
    update_date = str
    versioning = False
    state = int

    param_dxvk = False
    param_dxvk_hud = False
    param_sync = False
    param_aco_compiler = False
    param_discrete_gpu = False
    param_virtual_desktop = False
    param_virtual_desktop_res = str
    param_pulseaudio_latency = False
    param_fixme_logs = False
    param_environment_variables = str

    dependencies = []
    dll_overrides = {}
    programs = {}

    config_struct = {
        "Name": "",
        "Runner": "",
        "DXVK": "",
        "Path": "",
        "Environment": "",
        "Creation_Date": "",
        "Update_Date": "",
        "Versioning": False,
        "State": 0,
        "Parameters": {
            "dxvk": False,
            "dxvk_hud": False,
            "sync": "wine",
            "aco_compiler": False,
            "discrete_gpu": False,
            "virtual_desktop": False,
            "virtual_desktop_res": "1280x720",
            "pulseaudio_latency": False,
            "fixme_logs": False,
            "environment_variables": "",
        },
        "Installed_Dependencies": [],
        "DLL_Overrides": {},
        "Programs": {}
    }

    def __init__(self, path: str):
        self.path = path
        if not self.validate_bottle():
            raise ValueError("Given path doesn't seem a valid Bottle path.")

    def validate_bottle(self):
        '''
        Check if it is a valid bottle path.

        Return
        ----------
        bool
            True if it is a valid bottle path, otherwise False
        '''
        promise = ["dosdevices", "drive_c"]

        dirs = glob(f"{self.path}/*")
        dirs = [d.replace(f"{self.path}/", "") for d in dirs]

        for p in promise:
            if p not in dirs:
                return False

        '''
        Load config from path, if it not exists then create.
        '''
        try:
            file = open(f"{self.path}/bottle.json")
            config = json.load(file)
            file.close()
        except FileNotFoundError:
            file = open(f"{self.path}/bottle.json", "w")
            config = self.config_struct
            config["Name"] = f"Generated {randint(10000, 20000)}"
            config["Path"] = self.path
            # TODO: set runner to last installed
            json.dump(config, file, indent=4)
            config = json.load(file)
            file.close()

        '''
        Check for diffs. between config_struct and the bottle one, then update.
        '''
        missing_keys = self.config_struct.keys() - config.keys()
        for key in missing_keys:
            self.update_config(
                key=key,
                value=self.config_struct[key]
            )

        missing_keys = self.config_struct["Parameters"].keys(
        ) - config["Parameters"].keys()
        for key in missing_keys:
            self.update_config(
                key=key,
                value=self.config_struct[key],
                scope="Parameters"
            )

        return True

    def update_config(self, key: str, value: str, scope: str = None):
        '''
        Update keys for a bottle config file.

        Parameters
        ----------
        key : str
            the key name
        value : str
            the value to be set
        scope : str (optional)
            where to look for the key if it is not the root (default is None)
        '''
        if scope is not None:
            self.config[scope][key] = value
        else:
            self.config[key] = value

        file = open(f"{self.path}/bottle.json", "w")
        json.dump(self.config, file, indent=4)
        file.close()
