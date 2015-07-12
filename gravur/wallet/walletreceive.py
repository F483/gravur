# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import Screen
from common.navbar import NavBar  # NOQA
from common.labelbox import LabelBox  # NOQA
from common.amountinput import AmountInput  # NOQA
from common.storebutton import StoreButton  # NOQA
from common.addressdisplay import AddressDisplay  # NOQA
from contacts.selectcontact import SelectContact  # NOQA
from common.fadingtabedpanel import FadingTabbedPanel  # NOQA
from utils import load_widget


@load_widget
class WalletReceive(Screen):
    pass
