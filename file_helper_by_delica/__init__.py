from .file_helper_funcs import *
from importlib.metadata import version, PackageNotFoundError

__version__ = "unknown"
try:
    __version__ = version("test_helper_by_delica")
except PackageNotFoundError:
    pass

__all__ = ["file_helper_funcs"]
