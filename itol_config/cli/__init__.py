import argparse
from . import colour_strip
from . import text_label
from . import binary_data
from . import ranges

def cli():
    """Command-line interface for the itol_config package."""
    parser = argparse.ArgumentParser(
        description="Generate iTOL configuration files",
        prog="itol_config"
    )

    subparsers = parser.add_subparsers(
        title="subcommands",
        description="Different types of configuration files",
        help="sub-command help"
    )

    colour_strip.register_subparser(subparsers)
    text_label.register_subparser(subparsers)
    binary_data.register_subparser(subparsers)
    ranges.register_subparser(subparsers)


    args = parser.parse_args()
    if hasattr(args,"func"):
        args.func(args)
    else:
        parser.print_help()
