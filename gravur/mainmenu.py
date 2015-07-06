# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import Screen
from common.navbar import NavBar  # NOQA
from common.normalbutton import NormalButton  # NOQA
from utils import load_widget


@load_widget
class MainMenu(Screen):
    pass
