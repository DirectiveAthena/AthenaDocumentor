# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from enum import Enum
# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Types(Enum):
    """
    A simple data storage class to hold all tags meant to precede the object title.
    """
    fnc= "#func"
    cls= "#class"
    unknown="**!*UNKNOWN*!**"
    cls_mth = "#classmethod"
    stat_mth = "#staticmethod"
    module="#module"
    mth="#method"