#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import kivy
from kivy.app import App
from kivy.config import Config


# set to smallest supported resolution for now
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '460')


class GravurApp(App):
    pass


if __name__ == "__main__":
    GravurApp().run()
