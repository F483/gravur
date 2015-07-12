# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.actionbar import ActionBar
from kivy.properties import Property
from utils import load_widget


@load_widget
class NavBar(ActionBar):
    manager = Property(None)
