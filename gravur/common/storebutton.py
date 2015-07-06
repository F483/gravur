# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.button import Button
from kivy.properties import Property
from utils import load_widget


@load_widget
class StoreButton(Button):
    storebutton_text = Property('')
