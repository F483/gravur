# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.animation import Animation
from kivy.uix.tabbedpanel import TabbedPanel
from utils import load_widget


@load_widget
class FadingTabbedPanel(TabbedPanel):

    def __init__(self, *args, **kwargs):
        kwargs.update({"do_default_tab": False})
        super(FadingTabbedPanel, self).__init__(*args, **kwargs)

    #override tab switching method to animate on tab switch
    def switch_to(self, header):
        anim = Animation(opacity=0, d=.24, t='in_out_quad')

        def start_anim(_anim, child, in_complete, *lt):
            _anim.start(child)

        def _on_complete(*lt):
            if header.content:
                header.content.opacity = 0
                anim = Animation(opacity=1, d=.43, t='in_out_quad')
                start_anim(anim, header.content, True)
            super(FadingTabbedPanel, self).switch_to(header)

        anim.bind(on_complete=_on_complete)
        if self.current_tab.content:
            start_anim(anim, self.current_tab.content, False)
        else:
            _on_complete()
