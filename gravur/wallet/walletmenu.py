# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import Screen
from wallet.transactionlist import TransactionList  # NOQA
from common.labelbox import LabelBox  # NOQA
from common.navbar import NavBar  # NOQA
from common.normalbutton import NormalButton  # NOQA
from utils import load_widget


@load_widget
class WalletMenu(Screen):
    pass
