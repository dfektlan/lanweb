from django import template
from django.conf import settings
import urllib, hashlib

register = template.Library()

@register.assignment_tag(takes_context=True)


def get_gravatar_url(context, user, size):
    email = user.get_email()

    default = "https://dfektlan.no/media/nophoto.jpg"
    hash = hashlib.md5(email.lower()).hexdigest()
    print dir(context)

    gravatar_url = "https://www.gravatar.com/avatar/" + hash + "?"    
    gravatar_url += urllib.urlencode({'d': default, 's':str(size)})    

    return gravatar_url


def save_all_gravatars(size):
    from apps.userprofile.models import SiteUser
    import requests
    from io import open as iopen
    users = SiteUser.objects.all()

    for u in users:
        url = get_gravatar_url("derp", u, size)
        print url
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            print r.status_code
            with iopen(u.first_name + "_" + u.last_name + ".jpg", 'wb') as file:
                file.write(r.content)
