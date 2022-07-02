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
    else:
        return Types.unknown