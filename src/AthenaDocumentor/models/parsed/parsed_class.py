# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect
import types
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaDocumentor.models.parsed.parsed import Parsed
from AthenaDocumentor.models.parsed.parsed_method import ParsedMethod
from AthenaDocumentor.data.types import Types

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(init=False, eq=False)
class ParsedClass(Parsed):
    signature: inspect.Signature|None
    methods: list[ParsedMethod]

    def __init__(self, obj, parent_module):
        super(ParsedClass, self).__init__(obj,parent_module)
        try:
            self.signature = inspect.signature(obj)
        except ValueError:
            self.signature = None

        self.methods = [
            ParsedMethod(obj_method, parent_module)
            for name, obj_method in obj.__dict__.items()
            if isinstance(obj_method, classmethod|types.FunctionType|type)
        ]

    @property
    def type(self):
        return Types.cls

    def to_dict(self) -> dict:
        return super(ParsedClass, self).to_dict() | {
            "signature":str(self.signature),
            "methods":[method.to_dict() for method in self.methods]
        }