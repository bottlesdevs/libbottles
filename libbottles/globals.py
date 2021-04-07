from pathlib import Path


class Paths:
    # TODO: _base should change if flatpak or snap
    _base = f"{Path.home()}/.local/share/bottles"
    bottles = f"{_base}/bottles"
    components = f"{_base}/components"
