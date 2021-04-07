from pathlib import Path


class Paths:
    _base = f"{Path.home()}/.local/share/bottles"
    bottles = f"{_base}/bottles"
    components = f"{_base}/components"
