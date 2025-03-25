import argparse
from ..interfaces.ranges import RangeConfigWriter
from ..utils import load_data, sanitise
from ..colour import load_colour_conf

def run(args: argparse.Namespace) -> None:
    """
    Run the colour_strip subcommand
    
    Parameters
    ----------
    args : argparse.Namespace
        Arguments from the command-line
    """
    
    if args.colour_conf:
        colour_conf = load_colour_conf(args.colour_conf)
    else:
        colour_conf = {}
    
    
    data = load_data(args.input,args.id)
    for column in data:
        output_file = f"{args.output}.{sanitise(column)}.txt"
        writer = RangeConfigWriter(args.tree,data[column],column,colour_conf.get(column,None))
        writer.write(output_file)

def register_subparser(subparsers: argparse._SubParsersAction) -> None:
    """
    Register subparser for the itol_config package
    
    Parameters
    ----------
    subparser : argparse.ArgumentParser
        Subparser object for the itol_config package
    """
    subparser = subparsers.add_parser('ranges_label', help='Generate a text label configuration file')
    subparser.add_argument(
        "--input",
        help="Input file containing a csv file with sequence metadata",
        type=str,
        required=True
    )
    subparser.add_argument(
        "--tree",
        help="Input file containing a csv file with sequence metadata",
        type=str,
        required=True
    )
    subparser.add_argument(
        "--output",
        help="Output file name for the iTOL configuration file",
        type=str,
        required=True
    )
    subparser.add_argument(
        "--id",
        help="Column name matching the sequence IDs used in the tree",
        type=str,
        default="id"
    )
    subparser.add_argument(
        "--colour-conf",
        help="Colour configuration file",
        type=str,
        default=None
    )
    
    subparser.set_defaults(func=run)
