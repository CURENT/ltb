"""
LTB command-line interface and argument parsers.

Revised from ANDES.
"""

import argparse
import importlib
import logging
import platform
import sys
from time import strftime

import andes
import ams
import agvis

from ltb.main import config_logger, find_log_path
from andes.utils.paths import get_log_dir

logger = logging.getLogger(__name__)

command_aliases = {
    'selftest': ['st'],
}

def create_parser():
    """
    Create a parser for the command-line interface.

    Returns
    -------
    argparse.ArgumentParser
        Parser with all LTB options
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-v', '--verbose',
        help='Verbosity level in 10-DEBUG, 20-INFO, 30-WARNING, '
             'or 40-ERROR.',
        type=int, default=20, choices=(1, 10, 20, 30, 40))

    sub_parsers = parser.add_subparsers(dest='command', help='[demo] run demos; '
                                        )

    run = sub_parsers.add_parser('run')

    misc = sub_parsers.add_parser('misc')
    misc.add_argument('--license', action='store_true', help='Display software license', dest='show_license')
    misc.add_argument('-C', '--clean', help='Clean output files', action='store_true')
    misc.add_argument('-r', '--recursive', help='Recursively clean outputs (combined useage with --clean)',
                      action='store_true')
    misc.add_argument('--version', action='store_true', help='Display version information')

    doc = sub_parsers.add_parser('doc')

    plot = sub_parsers.add_parser('plot')

    selftest = sub_parsers.add_parser('selftest', aliases=command_aliases['selftest'])

    demo = sub_parsers.add_parser('demo')  # NOQA

    return parser


def preamble():
    """
    Log the LTB command-line preamble at the `logging.INFO` level
    """
    from ltb import __version__ as version

    py_version = platform.python_version()
    andes_version = andes.__version__
    ams_version = ams.__version__
    agvis_version = agvis.__version__
    system_name = platform.system()
    date_time = strftime('%m/%d/%Y %I:%M:%S %p')
    logger.info("\n"
                r" ██╗  ████████╗██████╗  | CURENT Large-scale Testbed Platform" + '\n'
                rf" ██║  ╚══██╔══╝██╔══██╗ | Version {version}" + '\n'
                rf" ██║     ██║   ██████╔╝ | ANDES {andes_version}; AMS {ams_version};" + "\n"
                rf" ██║     ██║   ██╔══██╗ | AGVis {agvis_version}; DiME;" + "\n"
                rf" ███████╗██║   ██████╔╝ | Python {py_version} on {system_name}, {date_time}" + "\n"
                r" ╚══════╝╚═╝   ╚═════╝  | This program comes with ABSOLUTELY NO WARRANTY." + '\n')

    log_path = find_log_path(logging.getLogger("ltb"))

    if len(log_path):
        logger.debug('Logging to file "%s"', log_path[0])


def main():
    """
    Entry point of the LTB command-line interface.
    """

    parser = create_parser()
    args = parser.parse_args()

    # Set up logging
    config_logger(stream=True,
                  stream_level=args.verbose,
                  file=True,
                  log_path=get_log_dir(),
                  )
    logger.debug(args)

    module = importlib.import_module('ltb.main')

    if args.command in ('plot', 'doc', 'misc'):
        pass
    elif args.command == 'run' and args.no_preamble is True:
        pass
    else:
        preamble()

    # Run the command
    if args.command is None:
        parser.parse_args(sys.argv.append('--help'))

    else:
        cmd = args.command
        for fullcmd, aliases in command_aliases.items():
            if cmd in aliases:
                cmd = fullcmd

        func = getattr(module, cmd)
        return func(cli=True, **vars(args))
