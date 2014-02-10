from django.shortcuts import render
import requests

import pprint

channels = {
    1: ['dfektlan', "dfekt LAN 1"],
    2: ['dfektlan2', "dfekt LAN 2"]
}


def stream(request, stream_id=None):
    if stream_id is None:
        stream_id = 1

    d = get_stream_as_dict(channels[int(stream_id)][0])


    if d:
        pprint.pprint(d)

        stream = {
            'name': get_name(d),
            'key': channels[int(stream_id)][0],
            'game': get_game(d),
            'status': get_status(d),
            'viewers': get_status(d),
            'views': get_views(d),
        }

    else:
        stream = {
            'name': channels[int(stream_id)][1],
            'key': channels[int(stream_id)][0],
            'game': 'Offline',
            'status': 'Offline',
            'viewers': 0,
            'views': 'Offline',
        }

    return render(request, 'tv/index.html', {'stream': stream, 'link': channels})


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