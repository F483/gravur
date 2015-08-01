# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import gravur
from gravur.mainmenu import MainMenu
from gravur.wallet.walletmenu import WalletMenu
from gravur.wallet.walletsend import WalletSend
from gravur.wallet.walletreceive import WalletReceive
from gravur.messanger.messangermenu import MessangerMenu
from gravur.messanger.broadcastmessage import BroadcastMessage
from gravur.messanger.viewmessage import ViewMessage
from gravur.messanger.privatemessage import PrivateMessage
from gravur.messanger.retrievefromtx import RetrieveFromTx
from gravur.signatures.signaturemenu import SignatureMenu
from gravur.signatures.signdocument import SignDocument
#from gravur.contacts.contactmenu import ContactMenu
from gravur.identities.identitymenu import IdentityMenu
from gravur.common.navbar import NavBar
from gravur.common.historicscreenmanager import HistoricScreenManager


class GravurApp(App):

    def __init__(self, backend_config):
        super(GravurApp, self).__init__()
        gravur.init_backend(backend_config)

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
        manager.add_widget(RetrieveFromTx(name='retrieve_form_tx'))
        manager.add_widget(ViewMessage(name='view_message'))

        manager.add_widget(SignatureMenu(name='signatures'))
        manager.add_widget(SignDocument(name='sign_document'))

        #manager.add_widget(ContactMenu(name='contacts'))
        manager.add_widget(IdentityMenu(name='identities'))

        # setup layout
        layout = BoxLayout(orientation='vertical')
        navbar = NavBar(manager=manager)
        layout.add_widget(navbar)
        layout.add_widget(manager)
        return layout
