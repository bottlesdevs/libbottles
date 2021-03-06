import yaml
from glob import glob
from datetime import datetime
from random import seed, randint
from libbottles.utils.checks import check_special_chars
from libbottles.components.runner import Runner

from libwine.wine import Wine

seed(1)


class Bottle:
    """
    Create a new object of type Bottle with all the methods for its management.

    Parameters
    ----------
    path : str
        the bottle full path
    """
    config: dict = {}
    _config_struct: dict = {
        "Name": "",
        "Runner": "",
        "DXVK": "",
        "Path": "",
        "Environment": 2,
        "Created": "",
        "Updated": "",
        "Versioning": False,
        "State": 0,
        "Verbose": 0,
        "Parameters": {
            "dxvk": False,
            "dxvk_hud": False,
            "sync": "wine",
            "aco_compiler": False,
            "discrete_gpu": False,
            "virtual_desktop": False,
            "virtual_desktop_res": "1280x720",
            "pulseaudio_latency": False,
            "environment_variables": "",
        },
        "Installed_Dependencies": [],
        "DLL_Overrides": {},
        "Programs": {}
    }
    _environments: dict = [
        {
            "Name": "Software",
            "Parameters": {
                "dxvk": True
            }
        },
        {
            "Name": "Gaming",
            "Parameters": {
                "dxvk": True,
                "sync": "esync",
                "discrete_gpu": True,
                "pulseaudio_latency": True
            }
        },
        {
            "Name": "Custom",
            "Parameters": {}
        }
    ]
    _supported_sync_types: dict = {
        0: "wine",
        1: "esync",
        2: "fsync"
    }
    wineprefix = object

    def __init__(
            self,
            path: str,
            create: bool = False,
            env: int = 3,
            name: str = None,
            runner_path: str = None,
            verbose: int = 0,
            versioning: bool = False):

        if not create:
            self.__validate(path)
            self.__load_config(path)
            self.__set_wineprefix(runner_path)
        else:
            self.config = {
                "Path": path,
                "Name": name,
                "Runner": runner_path,
                "Environment": env,
                "Verbose": verbose,
                "Versioning": versioning
            }
            self.__set_wineprefix(runner_path)
            self.wineprefix.update()
            self.__load_config(path)

            self.apply_environment(env)

    '''
    Bottle checks
    '''

    @staticmethod
    def __validate(path):
        """
        Check if essential paths exist in path.

        Parameters
        ----------
        path : str
            the bottle full path
        """
        promise = ["dosdevices", "drive_c"]

        dirs = glob(f"{path}/*")
        dirs = [d.replace(f"{path}/", "") for d in dirs]

        for p in promise:
            if p not in dirs:
                raise ValueError("Given path doesn't seem a valid Bottle path.")
        return True

    def __load_config(self, path):
        """
        Load config from path, if doesn't exists then create.
        Also update config structure if outdated.

        Parameters
        ----------
        path : str
            the bottle full path
        """
        try:
            file = open(f"{path}/bottle.yml")
            self.config = yaml.safe_load(file)
            file.close()
        except FileNotFoundError:
            file = open(f"{path}/bottle.yml", "w")

            if len(self.config) == 0:
                config = self._config_struct
                config["Name"] = f"Generated {randint(10000, 20000)}"
                config["Path"] = path
                config["Created"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                # TODO: set runner to latest installed

                yaml.dump(config, file, indent=4)
                self.config = yaml.safe_load(file)
            else:
                config = self.config
                yaml.dump(config, file, indent=4)

            file.close()

        '''
        Check for diffs. between _config_struct and the bottle one, then update.
        '''
        missing_keys = self._config_struct.keys() - self.config.keys()
        for key in missing_keys:
            self.update_config(
                key=key,
                value=self._config_struct[key]
            )

        missing_keys = (
                self._config_struct["Parameters"].keys() -
                self.config["Parameters"].keys()
        )
        for key in missing_keys:
            self.update_config(
                key=key,
                value=self._config_struct["Parameters"][key],
                scope="Parameters"
            )

    '''
    Wineprefix instance
    '''

    def __set_wineprefix(self, runner_path: str = None):
        if not runner_path:
            runner_path = self.config["Runner"]

        self.wineprefix = Wine(
            winepath=runner_path,
            wineprefix=self.config["Path"],
            verbose=self.config["Verbose"]
        )

    '''
    Bottle config tools
    '''

    def apply_environment(self, environment: int):
        if not self._environments[environment]:
            raise ValueError(f"{environment} is not a valid environment.")

        self.update_config(
            key="Environment",
            value=environment
        )
        # TODO: work in progress
        return

    def apply_config(self, config: dict):
        for key, value in config.items():
            self.update_config(
                key=key,
                value=value
            )

    def update_config(
            self,
            key: str = None,
            value: str = None,
            scope: str = None):
        """
        Update keys for a bottle config.

        Parameters
        ----------
        key : str
            the key name
        value : str
            the value to be set
        scope : str (optional)
            where to look for the key if it is not the root (default is None)
        """
        if scope is not None:
            self.config[scope][key] = value
        else:
            self.config[key] = value

        self.config["Updated"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        file = open(
            f"{self.config['Path']}/bottle.yml", "w")
        yaml.dump(self.config, file, indent=4)
        file.close()

    '''
    Bottle management
    '''

    def rename(self, name: str):
        if not check_special_chars(text=name):
            return self.update_config(
                key="Name",
                value=name
            )
        raise ValueError("The bottle name cannot contain special characters.")

    def set_runner(self):
        # TODO
        pass

    def set_versioning(self):
        # TODO
        pass

    def set_verbose(self, level: int):
        self.update_config(
            key="Verbose",
            value=level
        )
        self.wineprefix.set_verbose(level)

    def set_dxvk_hud(self, status: bool):
        self.update_config(
            key="dxvk_hud",
            value=status,
            scope="Parameters"
        )

    def set_sync(self, sync_type: int):
        if sync_type not in self._supported_sync_types:
            raise ValueError(f"{sync_type} is not a valid sync type.")

        self.update_config(
            key="sync",
            value=sync_type,
            scope="Parameters"
        )

    def set_aco_compiler(self, status: bool):
        self.update_config(
            key="aco_compiler",
            value=status,
            scope="Parameters"
        )

    def set_discrete_gpu(self, status: bool):
        self.update_config(
            key="discrete_gpu",
            value=status,
            scope="Parameters"
        )

    def set_virtual_desktop(self, status: bool):
        self.update_config(
            key="virtual_desktop",
            value=status,
            scope="Parameters"
        )
        if not status:
            self.wineprefix.set_virtual_desktop(False)

    def set_virtual_desktop_res(self, res: str):
        self.set_virtual_desktop(True)
        self.update_config(
            key="virtual_desktop_res",
            value=res,
            scope="Parameters"
        )
        self.wineprefix.set_virtual_desktop(
            status=True,
            res=res
        )

    def set_pulseaudio_latency(self, status: bool):
        self.update_config(
            key="pulseaudio_latency",
            value=status,
            scope="Parameters"
        )
