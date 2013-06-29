# -*- coding: utf-8 -*-
#from dfektlan import settings
from django.contrib.auth.models import Group
from userprofile.models import SiteUser
from crew.models import Application
from django.core.management import setup_environ


crews = ['Crew','Tech','Strøm','Kantine','Sikkerhet','Core','Game','Logistikk']

for i in crews:
    Group.objects.get_or_create(name=i)

users = ['thor','atle','anders','simen','bassan']
for i in users:
    SiteUser.objects.get_or_create(username=i, first_name=i, last_name=i[::-1], email=i+"dfektlan.no",  password=i, is_staff=True)

crew = [0,1,2,3,4,5]

for i in SiteUser.objects.all():
    for j in crew:
        Application.objects.get_or_create(user=i, about="lol", why="test", license="b", status=0, crew=j)
