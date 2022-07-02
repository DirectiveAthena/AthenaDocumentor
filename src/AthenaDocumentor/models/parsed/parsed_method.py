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

    def __init__(self, obj):
        super(ParsedMethod, self).__init__(obj)
        try:
            if isinstance(obj, classmethod|staticmethod):
                self.signature = inspect.signature(obj.__func__)
            else:
                self.signature = inspect.signature(obj)
        except ValueError:
            self.signature = None
        except AttributeError:
            print(obj)
            raise

    @property
    def type(self):
        return Types.mth

    def to_dict(self) -> dict:
        return super(ParsedMethod, self).to_dict() | {"signature":str(self.signature)}