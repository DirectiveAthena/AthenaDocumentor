# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import timeit

# Custom Library
import AthenaDocumentor

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main():
    parser = AthenaDocumentor.Parser(root_module=AthenaDocumentor).parse()
    parser.output_to_json_file("../exports/dump.json")
    parser.output_to_markdown_file(r"../exports\dump.md")


if __name__ == '__main__':
    print(timeit.repeat(lambda: main(), number=1_000, repeat=5))
    # [6.066017700002703, 5.930401899997378, 6.085921499994583, 6.7281146999957855, 6.086796099996718]