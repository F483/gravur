#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


# set to smallest supported resolution for now
from kivy.config import Config
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '460')


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from mainmenu import MainMenu
from wallet.walletmenu import WalletMenu
from wallet.walletsend import WalletSend
from wallet.walletreceive import WalletReceive
from messanger.messangermenu import MessangerMenu
from messanger.broadcastmessage import BroadcastMessage
from messanger.privatemessage import PrivateMessage
from notary.notarymenu import NotaryMenu
from notary.signdocument import SignDocument
from notary.createpoe import CreatePOE


class GravurApp(App):

    def build(self):
        sm = ScreenManager(transition=WipeTransition())

        sm.add_widget(MainMenu(name='mainmenu'))

        sm.add_widget(WalletMenu(name='wallet_menu'))
        sm.add_widget(WalletSend(name='wallet_send'))
        sm.add_widget(WalletReceive(name='wallet_receive'))

        sm.add_widget(MessangerMenu(name='messages'))
        sm.add_widget(BroadcastMessage(name='broadcast_message'))
        sm.add_widget(PrivateMessage(name='private_message'))

        sm.add_widget(NotaryMenu(name='notary'))
        sm.add_widget(SignDocument(name='sign_document'))
        sm.add_widget(CreatePOE(name='create_poe'))
        return sm


if __name__ == "__main__":
    GravurApp().run()
