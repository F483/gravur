# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import Screen
from gravur.wallet.transactionscrollview import TransactionScrollView  # NOQA
from gravur.wallet.invoicescrollview import InvoiceScrollView  # NOQA
from gravur.common.labelbox import LabelBox  # NOQA
from gravur.common.navbar import NavBar  # NOQA
from gravur.common.normalbutton import NormalButton  # NOQA
from gravur.common.fadingtabedpanel import FadingTabbedPanel  # NOQA
from gravur.utils import load_widget


@load_widget
class WalletMenu(Screen):
    pass
