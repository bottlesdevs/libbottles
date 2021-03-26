class Bottle:
    '''
    Create a new object of type Bottle with all the methods for its management.

    Parameters
    ----------
    pid : str
        the process id
    name: str
        the process name (command)
    parent_pid: str (optional)
        the parent process id
    wine: Wine
        the Wine object
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

    def __init__(self, path: str, generate: bool = False):
        pass

    def validate_bottle(self):
        '''
        TODO: validate_bottle()
        - check if config doens't exists in path
            - if generate == True: create config file in path
            - else: return False
        - check for update in config comparing with config_struct
            - if True: update
        '''
        return
