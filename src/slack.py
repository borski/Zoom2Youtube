# -*- coding: utf-8 -*-

from urllib.parse import urljoin

import requests


class SlackClient(object):
    BASE_URL = 'https://slack.com/api/'

    def __init__(self, token, bot_name=''):
        self.token = token
        self.bot_name = bot_name

    def chat_post_message(self, channel: str, text: str, **params):
        """https://api.slack.com/methods/chat.postMessage"""
        method = 'chat.postMessage'
        params.update({
            'channel': channel,
            'text': text,
        })
        return self._request(method, params)

    def send_message_to_channels(self, channels: list, text: str, **params):
        for channel in channels:
            self.chat_post_message(channel, text, **params)
            print('Download link sent to channel: {}'.format(channel))

    def _request(self, method, params):
        url = urljoin(SlackClient.BASE_URL, method)
        data = {'token': self.token}
        if self.bot_name:
            data['username'] = self.bot_name
        params.update(data)
        return requests.post(
            url,
            data=params,
            headers={'content-type': 'application/x-www-form-urlencoded'}
        )
