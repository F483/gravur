# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Property
from gravur.common.labelbox import LabelBox  # NOQA
from gravur.common.normalbutton import NormalButton  # NOQA
from gravur.utils import load_widget


@load_widget
class AddressDisplay(BoxLayout):
    address = Property('')
