#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import os
import sys
import argparse

# kivy setup
os.environ["KIVY_NO_ARGS"] = "1"
#os.environ["KIVY_NO_CONSOLELOG"] = "1"
os.environ["KIVY_NO_FILELOG"] = "1"

# min supported resolution
from kivy.config import Config
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '460')

# demo resolution
#from kivy.config import Config
#Config.set('graphics', 'width', '400')
#Config.set('graphics', 'height', '640')


from gravur.app import GravurApp


def _parse_args():
    class ArgumentParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    # setup parser
    description = "Gravur bitcoin wallet."
    parser = ArgumentParser(description=description)
    default_app_home = os.path.join(os.path.expanduser("~"), ".gravur")

    # wallet
    default_app_wallet = os.path.join(default_app_home, "default.wallet")
    parser.add_argument("--wallet", default=default_app_wallet, help="""
        Encrypted wallet file location (created if non existant).
        Default: {0}
    """.format(default_app_wallet))

    # testnet
    parser.add_argument('--testnet', action='store_true',
                        help="Use bitcoin testnet instead of mainnet.")

    # dryrun
    parser.add_argument('--dryrun', action='store_true',
                        help="Never publish anything to the blockchain.")

    # tmp_wallet
    parser.add_argument("temp_wallet", help="Temporary prototype wallet.")

    return vars(parser.parse_args())


if __name__ == "__main__":
    backend_config = _parse_args()
    GravurApp(backend_config).run()
