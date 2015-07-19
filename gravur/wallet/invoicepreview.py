# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Property
from gravur.common.labelbox import LabelBox  # NOQA
from gravur.utils import load_widget


@load_widget
class InvoicePreview(BoxLayout):

    txid = Property(None)
    timestamp = Property("loading")
    amount = Property("loading")

    def on_txid(self, instance, value):
        instance.timestamp = '2015-07-01 16:41'  # TODO get from txid
        instance.amount = '0.0012BTC'  # TODO get from txid
