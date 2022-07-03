# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaDocumentor.models.parsed.parsed import Parsed
from AthenaDocumentor.data.types import Types

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(init=False, eq=False)
class ParsedMethod(Parsed):
    """
    A dataclass for storage of method object components.
    Does not hold the documentation by itself, as this can often lead to memory overloads with large documentation strings

    Parameters:
    - obj: the method in question which must be stored
    - parent_module: the module where the class which holds the method in located in. This is a `types.ModuleType`
    """
    signature: inspect.Signature|None

    def __init__(self, obj, parent_module):
        self.obj = obj
        self.parent_module = parent_module
        self.module_name = parent_module.__name__
        try:
            if isinstance(obj, classmethod|staticmethod):
                self.obj_name = obj.__func__.__name__
                self.signature = inspect.signature(obj.__func__)
            else:
                self.obj_name = obj.__name__
                self.signature = inspect.signature(obj)
        except ValueError:
            self.signature = None

    @property
    def type(self):
        return Types.mth

    def to_dict(self) -> dict:
        return super(ParsedMethod, self).to_dict() | {"signature":str(self.signature)}