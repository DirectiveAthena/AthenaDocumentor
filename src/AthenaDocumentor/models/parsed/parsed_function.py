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
class ParsedFunction(Parsed):
    signature: inspect.Signature|None

    def __init__(self, obj,parent_module):
        super(ParsedFunction, self).__init__(obj, parent_module)
        try:
            self.signature = inspect.signature(obj)
        except ValueError:
            self.signature = None

    @property
    def type(self):
        return Types.fnc

    def to_dict(self) -> dict:
        return super(ParsedFunction, self).to_dict() | {"signature":str(self.signature)}