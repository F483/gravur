# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


class AbstractScrollView(ScrollView):

    def __init__(self, *args, **kwargs):

        # Setup scroll view
        kwargs.update({
            "pos_hint": {'center_x': 0.5, 'center_y': 0.5},
            "do_scroll_x": False
        })
        super(AbstractScrollView, self).__init__(*args, **kwargs)

        # create layout
        layout = GridLayout(cols=kwargs.get("cols", 1),
                            padding=kwargs.get("padding", 0),
                            spacing=kwargs.get("spacing", 0),
                            size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # add widgets to layout
        entry_widget = kwargs['entry_widget']
        entries = kwargs.get('entries', [])
        for widget_kwargs in entries:
            widget_kwargs.update({"size_hint_y": None})
            layout.add_widget(entry_widget(**widget_kwargs))

        # add layout
        self.add_widget(layout)
