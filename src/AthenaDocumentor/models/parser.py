# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import copy
import json
import inspect

# Custom Library

# Custom Packages
from AthenaDocumentor.models.parsed_data import ParsedObject
from AthenaDocumentor.models.markdown_structure import MarkdownStructure
from AthenaDocumentor.data.types import Types

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, eq=False)
class Parser:
    """
    Object to control the correct handling of parsing through a Python package
    """
    root_module:Any
    markdown_structure:type[MarkdownStructure]=field(default=MarkdownStructure)

    # non init
    parsed_items:dict[str:list[ParsedObject]]=field(init=False, default_factory=dict)
    handled_components:set=field(init=False, default_factory=set)
    root_module_imports:list=field(init=False, default_factory=list)

    def parse(self) -> Parser:
        """
        Main method of the Parser object.
        Running this will start the pared and populate the 'parsed_items' slot of the Parser object
        """
        self.root_module_imports = [i for i in dir(self.root_module) if not i.startswith("__")]
        self.parsed_items[self.root_module.__name__] = []

        self._parse_recursive(self.root_module)
        return self

    def _parse_recursive(self, module_to_parse:Any):
        for component in dir(module_to_parse): #type:str
            # skip special dunder components in a module
            if component.startswith("__") or component in self.handled_components:
                continue
            # store component string to skip the same name in the future
            self.handled_components.add(component)

            # get that actual attribute object
            #   This is needed for the actual storage of component information
            if inspect.ismodule(attr := getattr(module_to_parse, component)):
                self._parse_recursive(attr)

            elif inspect.isclass(attr) or inspect.isfunction(attr) or inspect.ismethod(attr):
                # don't store components which are not a native part of the root module
                if not (parsed_attr := ParsedObject(attr)).module_name.startswith(self.root_module.__name__):
                    continue

                # make sure the module name is in the dictionary else it will fail
                elif parsed_attr.module_name not in self.parsed_items:
                    self.parsed_items[parsed_attr.module_name] = []

                # fixes the issue that root imported objects/classes/etc... weren't displayed as such
                if component in self.root_module_imports:
                    parsed_attr.parent_module = self.root_module
                    self.parsed_items[self.root_module.__name__].append(parsed_attr)
                else:
                    self.parsed_items[parsed_attr.module_name].append(parsed_attr)


    def output_to_dict(self, *, flat:bool=False) -> dict[str:list[dict]]:
        """
        Output the 'parsed_items' dictionary as is, or with custom parameters.
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
        """
        with open(filepath, "w+") as file:
            file.write(
                json.dumps(
                    self.output_to_dict(flat=True),
                    indent=4
                )
            )

    def output_to_markdown_file(self, filepath:str):
        """
        Output the 'parsed_items' to a structured markdown file.
        """
        with open(filepath, "w+") as file:
            for module_name, module_list in self.parsed_items.items(): #type: str, list[ParsedObject]
                for module in module_list:
                    match module:
                        case ParsedObject(type=Types.cls):
                            file.write(self.markdown_structure.structure_class(module))
                        case ParsedObject(type=Types.fnc):
                            file.write(self.markdown_structure.structure_function(module))



