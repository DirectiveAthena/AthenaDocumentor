# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
import inspect
from typing import Any
from types import ModuleType

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, init=False)
class ParsedObject:
    name:str
    doc:str
    parent_module:ModuleType
    signature:inspect.Signature
    methods:list[ParsedObject]

    def __init__(self, obj):
        if not (inspect.isclass(obj) or inspect.isfunction(obj) or inspect.ismodule(obj)):
            raise TypeError

        self.name = obj.__name__
        doc = inspect.getdoc(obj)
        if doc is not None:
            doc = inspect.cleandoc(doc)
        self.doc = doc
        self.parent_module = inspect.getmodule(obj)
        self.signature = inspect.signature(obj)

        self.methods = [
            ParsedObject(obj_method)
            for name, obj_method in obj.__dict__.items()
            if (inspect.ismethod(obj_method) or inspect.isfunction(obj_method))
        ]

    def to_dict(self) -> dict:
        return {
            "name":self.name,
            "doc":self.doc,
            "parent_module":self.parent_module.__name__,
            "signature":str(self.signature),
            "methods": [method.to_dict() for method in self.methods]
        }