# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from common.abstractscrollview import AbstractScrollView
from messanger.messagepreview import MessagePreview
from utils import load_widget


@load_widget
class MessageScrollView(AbstractScrollView):

    def __init__(self, *args, **kwargs):

        # TODO get entries from btctxstore
        id = 'e30fa138367bc73b2174f54bd4cf307521ba26fe91539e0a77e22d3dd2cdbc03'
        entries = [{'txid': id} for i in range(100)]

        kwargs.update({
            'spacing': 1,
            'entry_widget': MessagePreview,
            'entries': entries
        })
        super(MessageScrollView, self).__init__(*args, **kwargs)
