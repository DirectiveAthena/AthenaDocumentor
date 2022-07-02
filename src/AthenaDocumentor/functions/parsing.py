# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect

# Custom Library

# Custom Packages
from AthenaDocumentor.models.parsed import Parsed, ParsedModule, ParsedMethod,ParsedClass,ParsedFunction

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def parser(obj:object|type) -> Parsed|None:
    if inspect.isbuiltin(obj):
        return
    if inspect.isclass(obj):
        return ParsedClass(obj)
    elif inspect.isfunction(obj):
        return ParsedFunction(obj)
    elif inspect.ismethod(obj):
        return ParsedMethod(obj)
    elif inspect.ismodule(obj):
        return ParsedModule(obj)