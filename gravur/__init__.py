# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from btctxstore import BtcTxStore


backend = None
temp_wallet = None


def init_backend(config):
    global backend
    global temp_wallet
    backend = BtcTxStore(
        testnet=config["testnet"],
        dryrun=config["dryrun"],
        # TODO wallet_path=config["wallet"],
    )
    temp_wallet = config["temp_wallet"]

