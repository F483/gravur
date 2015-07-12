# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import Screen
from common.navbar import NavBar  # NOQA
from common.normalbutton import NormalButton  # NOQA
from common.labelbox import LabelBox  # NOQA
from common.eigengraubox import EigengrauBox  # NOQA
from common.amountinput import AmountInput  # NOQA
from common.storebutton import StoreButton  # NOQA
from contacts.selectcontact import SelectContact  # NOQA
from common.fadingtabedpanel import FadingTabbedPanel  # NOQA
from utils import load_widget


@load_widget
class WalletSend(Screen):
    pass
