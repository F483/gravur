# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Property
from common.labelbox import LabelBox  # NOQA
from utils import load_widget


@load_widget
class SignaturePreview(BoxLayout):

    txid = Property(None)
    timestamp = Property("loading")
    alias = Property("loading")
    address = Property("loading")
    signature = Property("loading")
    document_name = Property("loading")
    sha256sum = Property("loading")

    def on_txid(self, instance, value):
        instance.timestamp = '2015-07-01 16:41'  # TODO get from txid
        instance.alias = 'fabe'  # TODO get from txid
        instance.address = 'mjuqsdRQvSXhspK5D4koD3WUwy6R7ZtvXs'  # TODO get from txid
        instance.signature = "signature"  # TODO get from txid
        instance.document_name = "document name"  # TODO get from txid
        instance.sha256sum = "sha256sum"  # TODO get from txid
