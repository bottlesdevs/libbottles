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
    config = {}
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
        self.__validate_bottle(path)
        self.__load_config(path)

    def __validate_bottle(self, path):
        '''
        Check if essential paths exist in path.

        Parameters
        ----------
        path : str
            the bottle full path
        '''
        promise = ["dosdevices", "drive_c"]

        dirs = glob(f"{path}/*")
        dirs = [d.replace(f"{path}/", "") for d in dirs]

        for p in promise:
            if p not in dirs:
                raise ValueError("Given path doesn't seem a valid Bottle path.")
        return True

    def __load_config(self, path):
        '''
        Load config from path, if doesn't exists then create.
        Also update config structure if outdated.

        Parameters
        ----------
        path : str
            the bottle full path
        '''
        try:
            file = open(f"{path}/bottle.json")
            self.config = json.load(file)
            file.close()
        except FileNotFoundError:
            file = open(f"{path}/bottle.json", "w")
            config = self.config_struct
            config["Name"] = f"Generated {randint(10000, 20000)}"
            config["Path"] = path
            # TODO: set runner to last installed
            json.dump(config, file, indent=4)
            self.config = json.load(file)
            file.close()

        '''
        Check for diffs. between config_struct and the bottle one, then update.
        '''
        missing_keys = self.config_struct.keys() - self.config.keys()
        for key in missing_keys:
            self.update_config(
                key=key,
                value=self.config_struct[key]
            )

        missing_keys = (
            self.config_struct["Parameters"].keys() -
            self.config["Parameters"].keys()
        )
        for key in missing_keys:
            self.update_config(
                key=key,
                value=self.config_struct["Parameters"][key],
                scope="Parameters"
            )

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

        file = open(f"{self.config['Path']}/bottle.json", "w")
        json.dump(self.config, file, indent=4)
        file.close()
