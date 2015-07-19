# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import Screen
from gravur.common.navbar import NavBar  # NOQA
from gravur.common.normalbutton import NormalButton  # NOQA
from gravur.utils import load_widget


@load_widget
class MainMenu(Screen):
    pass
