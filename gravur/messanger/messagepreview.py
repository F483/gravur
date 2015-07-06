# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Property
from common.labelbox import LabelBox  # NOQA
from utils import load_widget


DUMMY_MESSAGE = """Lorem Ipsum is simply dummy text of the printing
and typesetting industry. Lorem Ipsum has been the industry's standard
dummy text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book. It has survived
not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with
the release of Letraset sheets containing Lorem Ipsum passages, and
more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum."""


@load_widget
class MessagePreview(BoxLayout):

    txid = Property(None)
    timestamp = Property("loading")
    alias = Property("loading")
    address = Property("loading")
    message = Property("loading")

    def on_txid(self, instance, value):
        instance.timestamp = '2015-07-01 16:41'  # TODO get from txid
        instance.alias = 'fabe'  # TODO get from txid
        instance.address = 'mjuqsdRQvSXhspK5D4koD3WUwy6R7ZtvXs'  # TODO get from txid
        instance.message = DUMMY_MESSAGE.replace("\n", " ")  # TODO get from txid
