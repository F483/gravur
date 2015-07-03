#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)

from kivy.config import Config

# set to smallest supported resolution for now
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '460')


from kivy.app import App
from kivy.properties import Property
from kivy.uix.actionbar import ActionBar
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition


class NavBar(ActionBar):
    pass


class SelectContact(BoxLayout):
    pass


class AmountInput(BoxLayout):
    pass


class AddressDisplay(BoxLayout):
    title = Property('')
    address = Property('')
    amount = Property('')


class LabelBox(Label):
    pass


class StoreButton(Button):
    storebutton_text = Property('')


class NormalButton(Button):
    normalbutton_text = Property('')


class MainScreen(Screen):
    pass


class MessagesScreen(Screen):
    pass


class BroadcastMessageScreen(Screen):
    pass


class PrivateMessageScreen(Screen):
    pass


class NotaryScreen(Screen):
    pass


class WalletScreen(Screen):
    pass


class WalletSendScreen(Screen):
    pass


class WalletReceiveScreen(Screen):
    pass


class SignDocumentScreen(Screen):
    pass


class CreatePOEScreen(Screen):
    pass


class GravurApp(App):

    def build(self):
        sm = ScreenManager(transition=WipeTransition())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(MessagesScreen(name='messages'))
        sm.add_widget(BroadcastMessageScreen(name='broadcast_message'))
        sm.add_widget(PrivateMessageScreen(name='private_message'))
        sm.add_widget(NotaryScreen(name='notary'))
        sm.add_widget(WalletScreen(name='wallet'))
        sm.add_widget(WalletSendScreen(name='wallet_send'))
        sm.add_widget(WalletReceiveScreen(name='wallet_receive'))
        sm.add_widget(SignDocumentScreen(name='sign_document'))
        sm.add_widget(CreatePOEScreen(name='create_poe'))
        return sm


if __name__ == "__main__":
    GravurApp().run()

