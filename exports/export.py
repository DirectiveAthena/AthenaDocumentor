# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaDocumentor

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    parser = AthenaDocumentor.Parser(root_module=AthenaDocumentor).parse()
    # output the entire AthenaDocumentor to JSON
    parser.output_to_json_file("dump.json")

    # output the entire AthenaDocumentor to MarkDown
    parser.output_to_markdown_file("dump.md")

if __name__ == '__main__':
    main()