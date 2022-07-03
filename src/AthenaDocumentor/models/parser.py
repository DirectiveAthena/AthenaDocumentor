# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import copy
import json
import types
import inspect

# Custom Library

# Custom Packages
from AthenaDocumentor.models.outputs.output import Output
from AthenaDocumentor.models.outputs.output_markdown import OutputMarkdown
from AthenaDocumentor.models.parsed import Parsed, ParsedModule, ParsedMethod,ParsedClass,ParsedFunction


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, eq=False)
class Parser:
    """
    Object to control the correct handling of parsing through a Python package

    Parameters:
    - root_module: `types.ModuleType`
    - markdown_structure: `AthenaDocumentor.OutputMarkdown`
    - parse_items_with_underscore: `bool` -> Boolean option whether to implement single underscored objects in parsing

    """
    root_module:types.ModuleType
    markdown_structure:type[Output]=field(default=OutputMarkdown)
    parse_items_with_underscore:bool=True

    # non init
    parsed_items:dict[str:list[Parsed]]=field(init=False)
    handled_components:set=field(init=False, default_factory=set)
    allowed_roots_imports:list=field(init=False)

    def __post_init__(self):
        self.allowed_roots_imports = [
            getattr(self.root_module, i).__name__
            for i in dir(self.root_module)
            if not i.startswith("__")
        ]
        self.parsed_items = {self.root_module.__name__:[]}


    def parse(self) -> Parser:
        """
        Main method of the Parser object.
        Running this will start the pared and populate the 'parsed_items' slot of the Parser object
        """
        self._parse_recursive(self.root_module)
        return self

    def _parse_recursive(self, module_to_parse:Any):
        for component in (c for c in dir(module_to_parse) if c not in self.handled_components): #type:str
            # store component string to skip the same name in the future
            self.handled_components.add(component)

            # skip special dunder components in a module
            if component.startswith("__") \
            or (component.startswith("_") and not self.parse_items_with_underscore):
                continue

            # retrieve actual objects
            obj = getattr(module_to_parse, component)
            parent_module = inspect.getmodule(obj)

            # check objects
            if inspect.isbuiltin(obj) \
            or parent_module is None \
            or not parent_module.__name__.startswith(self.root_module.__name__):
                continue
            elif inspect.isclass(obj):
                parsed_attr = ParsedClass(obj,parent_module)
            elif inspect.isfunction(obj):
                parsed_attr = ParsedFunction(obj,parent_module)
            elif inspect.ismethod(obj):
                parsed_attr = ParsedMethod(obj,parent_module)
            elif inspect.ismodule(obj):
                self._parse_recursive(ParsedModule(obj, parent_module).obj)
                continue
            else:
                continue

            # fixes the issue that root imported objects/classes/etc... weren't displayed as such
            # print(parsed_attr.obj_name, self.allowed_roots_imports)
            if parsed_attr.obj_name in self.allowed_roots_imports:
                parsed_attr.parent_module = self.root_module
                self.parsed_items[self.root_module.__name__].append(parsed_attr)
            # make sure the module name is in the dictionary else it will fail
            elif parsed_attr.module_name not in self.parsed_items:
                self.parsed_items[parsed_attr.module_name] = [parsed_attr]
            else:
                self.parsed_items[parsed_attr.module_name].append(parsed_attr)

    # ------------------------------------------------------------------------------------------------------------------
    # - Outputs -
    # ------------------------------------------------------------------------------------------------------------------
    def output_to_dict(self, *, flat:bool=False) -> dict[str:list[dict]]:
        """
        Output the 'parsed_items' dictionary as is, or with custom parameters.

        Parameters:
        - flat: bool -> Will return the `self.parsed_items` as is, calling the `to_dict()` method on all Parsed objects
        """
        if not flat:
            return copy.deepcopy(self.parsed_items)
        # else:
        return {
            k: [v_.to_dict() for v_ in v]
            for k,v in self.parsed_items.items()
        }

    def output_to_json_file(self, filepath:str):
        """
        Output the 'parsed_items' dictionary to a json file.
        This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`

        Parameters:
        - filepath -> The file to write to
        """
        with open(filepath, "w+") as file:
            file.write(
                json.dumps(
                    self.output_to_dict(flat=True),
                    indent=4
                )
            )

    def output_to_json_string(self) -> str:
        """
        Output the 'parsed_items' dictionary to a json formatted string.
        This method calls the `self.output_to_dict` method with the 'flat' parameter set to `True`
        """
        return json.dumps(
            self.output_to_dict(flat=True),
            indent=4
        )

    def _output_to_markdown(self):
        for module_name, module_list in self.parsed_items.items():  # type: str, list[Parsed]
            for module in module_list:
                match module:
                    case ParsedClass():
                        yield self.markdown_structure.structure_class(module)
                    case ParsedFunction():
                        yield self.markdown_structure.structure_function(module)
                    case ParsedMethod():
                        yield self.markdown_structure.structure_function(module)
                    case ParsedModule():
                        continue
                    case _:
                        raise TypeError(module)
                    # case Parse:
                    #     yield self.markdown_structure.structure_function(module)

    def output_to_markdown_file(self, *filepath:str):
        """
        Output the 'parsed_items' to a structured MarkDown file.

        Parameters:
        - filepath -> The file to write to
        """
        for fp in filepath:
            with open(fp, "w+") as file:
                for n in self._output_to_markdown():
                    file.write(n)

    def output_to_markdown_string(self) -> str:
        """
        Output the 'parsed_items' to string, formatted in MarkDown
        """
        return "".join(self._output_to_markdown())




