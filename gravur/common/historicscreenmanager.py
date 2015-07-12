# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.screenmanager import ScreenManager


class HistoricScreenManager(ScreenManager):

    def __init__(self, *args, **kwargs):
        super(HistoricScreenManager, self).__init__(*args, **kwargs)
        self.screen_history = []

    def on_current(self, instance, value):
        super(HistoricScreenManager, self).on_current(instance, value)
        self.screen_history.append(value)

    def switch_to_preceding(self):
        if len(self.screen_history) > 1:
            previous_screen = self.screen_history[-2]
            self.screen_history = self.screen_history[:-2]
            self.current = previous_screen

    def switch_to_root(self):
        if len(self.screen_history) > 0:
            root = self.screen_history[0]
            self.screen_history = []
            self.current = root
