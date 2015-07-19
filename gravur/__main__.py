#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


# set to smallest supported resolution for now
from kivy.config import Config
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '460')


from gravur.app import GravurApp


if __name__ == "__main__":
    GravurApp().run()
