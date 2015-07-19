# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import Screen
from gravur.common.navbar import NavBar  # NOQA
from gravur.common.storebutton import StoreButton  # NOQA
from gravur.common.labelbox import LabelBox  # NOQA
from gravur.utils import load_widget
import gravur


@load_widget
class BroadcastMessage(Screen):
    
    def broadcast_message(self, message):

        # create and send tx
        sender = gravur.temp_wallet
        wifs = [gravur.temp_wallet]
        txid = gravur.backend.store_broadcast_message(message, sender, wifs)
        print("txid:", txid)

        # switch to view message screen
        screen = self.manager.get_screen('view_message')
        screen.txid = txid
        self.manager.current = 'view_message'

        # TODO clear input properties
