from django.shortcuts import render
from apps.tv.models import Channel
import requests

import pprint

#channels = {
#    1: ['dfektlan', "dfekt LAN 1"],
#    2: ['dfektlan2', "dfekt LAN 2"]
#}


def stream(request, event=None, stream_id=None):
    channels = Channel.objects.all()
    if stream_id is None:
        stream_id = 1

    channel = channels.get(pk=stream_id)
    print channel.channelName
    d = get_stream_as_dict(channel.channelName)
    pprint.pprint(d)

    if d:
        stream = {
            'name': channel.displayName,
            'key': channel.channelName,
            'game': get_game(d),
            'status': get_status(d),
            'viewers': get_status(d),
            'views': get_views(d),
        }

    else:
        stream = {
            'name': channel.displayName,
            'key': channel.channelName,
            'game': 'Offline',
            'status': 'Offline',
            'viewers': 0,
            'views': 'Offline',
        }

    links = []
    for channel in channels:
        links.append((channel.pk, channel.displayName))

    return render(request, 'tv/index.html', {'stream': stream, 'link': links, 'event': event})


def get_stream_as_dict(channel):
    req = requests.get("https://api.twitch.tv/kraken/streams/%s" % (channel, ))
    if req.json()['stream']:
        return req.json()
    return None


def get_name(d):
    return d['stream']['channel']['display_name']


def get_game(d):
    return d['stream']['game']


#def get_chat(d):
#    return d['stream']['channel']['']['chat']


def get_status(d):
    return d['stream']['channel']['status']


def get_viewers(d):
    return d['stream']['viewers']


def get_views(d):
    return d['stream']['channel']['views']
