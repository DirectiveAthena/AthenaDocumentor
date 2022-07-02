# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
import inspect
from types import ModuleType
# Custom Library

# Custom Packages
from AthenaDocumentor.functions.type_finder import find_type
from AthenaDocumentor.data.types import Types

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, init=False)
class ParsedObject:
    name:str
    module_name:str
    doc:str
    parent_module:ModuleType
    signature:inspect.Signature|None
    methods:list[ParsedObject]
    type:Types

    def __init__(self, obj):
        if not any((inspect.isclass(obj), inspect.ismodule(obj), inspect.isfunction(obj))):
            raise TypeError

        self.name = obj.__name__
        doc = inspect.getdoc(obj)
        if doc is not None:
            doc = inspect.cleandoc(doc)
        self.doc = doc
        self.parent_module = inspect.getmodule(obj)
        try:
            self.signature = inspect.signature(obj)
        except ValueError:
            self.signature = None
        self.module_name = inspect.getmodule(obj).__name__

        self.methods = [
            ParsedObject(obj_method)
            for name, obj_method in obj.__dict__.items()
            if (inspect.ismethod(obj_method) or inspect.isfunction(obj_method))
        ]

        self.type = find_type(obj)

    def to_dict(self) -> dict:
        return {
            "type":self.type.value,
            "name":self.name,
            "doc":self.doc,
            "parent_module":self.parent_module.__name__,
            "signature":str(self.signature),
            "methods": [method.to_dict() for method in self.methods]
        }