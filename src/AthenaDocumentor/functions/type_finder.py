# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect

# Custom Library

# Custom Packages
from AthenaDocumentor.data.types import Types

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def find_type(obj) -> Types:
    if inspect.isclass(obj):
        return Types.cls
    elif inspect.isfunction(obj) or inspect.ismethod(obj):
        return Types.fnc
    elif isinstance(obj, staticmethod):
        return Types.stat_mth
    elif isinstance(obj, classmethod):
        return Types.cls_mth
    else:
        return Types.unknown