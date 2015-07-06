# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.boxlayout import BoxLayout
from common.labelbox import LabelBox  # NOQA
from wallet.transactionscrollview import TransactionScrollView  # NOQA
from utils import load_widget


@load_widget
class TransactionList(BoxLayout):
    pass
