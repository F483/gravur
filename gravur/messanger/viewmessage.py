# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import Screen
from kivy.properties import Property
from gravur.common.navbar import NavBar  # NOQA
from gravur.common.labelbox import LabelBox  # NOQA
from gravur.utils import load_widget
import gravur


@load_widget
class ViewMessage(Screen):
    txid = Property('')
    message = Property('')
    address = Property('')
    signature = Property('')
    timestamp = Property("YYYY-MM-DD HH:MM")
    alias = Property("TODO alias")
    message_type = Property("")

    def on_txid(self, instance, value):
        result = gravur.backend.retrieve_broadcast_message(value)
        self.address = result["address"]
        self.message = result["message"]
        self.signature = result["signature"]
        self.message_type = "BC"
        # TODO set timestamp, alias

    def display(self, txid):
        self.txid = txid
        self.manager.current = 'view_message'
