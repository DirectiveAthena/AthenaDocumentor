# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import inspect
from types import ModuleType
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaDocumentor.data.types import Types

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(init=False, eq=False)
class Parsed(ABC):
    obj:Any
    obj_name:str
    parent_module:ModuleType|None
    module_name:str

    def __init__(self, obj, parent_module):
        self.obj = obj
        self.obj_name = obj.__name__
        self.parent_module = parent_module
        self.module_name =parent_module.__name__

    @property
    @abstractmethod
    def type(self) -> Types:
        pass

    def to_dict(self) -> dict:
        return {
            "type":self.type.value,
            "name":self.obj_name,
            "doc":inspect.getdoc(self.obj),
            "parent_module":self.parent_module.__name__
        }