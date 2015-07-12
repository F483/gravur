#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


# set to smallest supported resolution for now
from kivy.config import Config
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '460')


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from mainmenu import MainMenu
from wallet.walletmenu import WalletMenu
from wallet.walletsend import WalletSend
from wallet.walletreceive import WalletReceive
from messanger.messangermenu import MessangerMenu
from messanger.broadcastmessage import BroadcastMessage
from messanger.privatemessage import PrivateMessage
from signatures.signaturemenu import SignatureMenu
from signatures.signdocument import SignDocument
from common.navbar import NavBar
from common.historicscreenmanager import HistoricScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class GravurApp(App):

    def build(self):

        # setup screens
        manager = HistoricScreenManager()

        manager.add_widget(MainMenu(name='mainmenu'))

        manager.add_widget(WalletMenu(name='wallet_menu'))
        manager.add_widget(WalletSend(name='wallet_send'))
        manager.add_widget(WalletReceive(name='wallet_receive'))

        manager.add_widget(MessangerMenu(name='messages'))
        manager.add_widget(BroadcastMessage(name='broadcast_message'))
        manager.add_widget(PrivateMessage(name='private_message'))

        manager.add_widget(SignatureMenu(name='signatures'))
        manager.add_widget(SignDocument(name='sign_document'))

        # setup layout
        layout = BoxLayout(orientation='vertical')
        navbar = NavBar(manager=manager)
        layout.add_widget(navbar)
        layout.add_widget(manager)
        return layout


if __name__ == "__main__":
    GravurApp().run()
