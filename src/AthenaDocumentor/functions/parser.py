# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect
from types import ModuleType

# Custom Library

# Custom Packages
from AthenaDocumentor.models.parsed_data import ParsedObject

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
memory = set()
root_module:ModuleType|None=None
fully_parsed:dict = {}

def _parse_recursive(module_, *, to_dict:bool=False):
    global root_module
    global fully_parsed
    global memory

    for i in dir(module_):
        if i.startswith("__") or i in memory:
            continue

        memory.add(i)

        attr:object = getattr(module_, i)
        if inspect.ismodule(attr):
            _parse_recursive(attr, to_dict=to_dict)

        elif inspect.isclass(attr) or  inspect.isfunction(attr) or inspect.ismethod(attr):
            parsed_attr = ParsedObject(attr)

            if parsed_attr.module_name.startswith(root_module.__name__):
                if parsed_attr.module_name in fully_parsed:
                    fully_parsed[parsed_attr.module_name].append(parsed_attr.to_dict() if to_dict else parsed_attr)
                else:
                    fully_parsed[parsed_attr.module_name] = [parsed_attr.to_dict() if to_dict else parsed_attr]

def parse_all(module_, *, to_dict:bool=False) -> fully_parsed:
    global root_module
    global fully_parsed
    global memory

    if root_module is None:
        root_module = module_

    _parse_recursive(module_, to_dict=to_dict)

    return fully_parsed