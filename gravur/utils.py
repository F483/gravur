# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import os
from kivy.lang import Builder
from kivy.factory import Factory


def load_widget(widget_class):
    path = os.path.join(*widget_class.__module__.split(".")) + ".kv"
    if os.path.exists(os.path.join(os.getcwd(), "gravur", path)):
        Builder.load_file(path)
    Factory.register(widget_class.__name__, cls=widget_class)
    return widget_class

