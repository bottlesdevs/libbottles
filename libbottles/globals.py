from pathlib import Path


class Paths:
    # TODO: _base should change if flatpak or snap
    _base = f"{Path.home()}/.local/share/bottles"
    bottles = f"{_base}/bottles"
    components = f"{_base}/components"
    runners = f"{components}/runners"
    dxvks = f"{components}/dxvks"


class Repository:
    _base = "https://raw.githubusercontent.com/bottlesdevs"
    components = f"{_base}/components/main"
    components_index = f"{components}/index.json"
