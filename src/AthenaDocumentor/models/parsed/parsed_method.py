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