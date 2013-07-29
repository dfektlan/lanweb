# -*- coding: utf-8 -*-
#from dfektlan import settings
from django.contrib.auth.models import Group
from userprofile.models import SiteUser
from crew.models import Application
from django.core.management import setup_environ
from news.models import Post
from django.template.defaultfilters import slugify
from event.models import LanEvent
from datetime import datetime


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lobortis leo ut eleifend vulputate. Aliquam sodales, nisi quis suscipit semper, magna mi vestibulum velit, at mattis libero justo quis nunc. Suspendisse porta odio molestie, consequat nunc at, dignissim dolor. Sed commodo purus nibh, quis lacinia dui consectetur sit amet. Mauris porttitor tincidunt adipiscing. Donec ac molestie turpis. Aliquam accumsan dignissim erat fringilla ultricies. Nam tempus ligula eget dolor tempor iaculis. Etiam ut consectetur magna. Praesent eu ipsum viverra, molestie dolor sit amet, elementum augue. Nulla mi enim, dapibus nec ligula sit amet, dignissim tincidunt dui. Nulla egestas enim quis sagittis blandit. Sed a nibh non turpis porttitor tincidunt in at nibh."
crews = ['Crew','Tech','Strøm','Kantine','Sikkerhet','Core','Game','Logistikk','Deltager']

for i in crews:
    Group.objects.get_or_create(name=i)

users = ['thor','atle','anders','simen','bassan']
for i in users:
    SiteUser.objects.get_or_create(username=i, first_name=i, last_name=i[::-1], email=i+"dfektlan.no",  password=i, is_staff=True)

crew = [0,1,2,3,4,5]

for i in SiteUser.objects.all():
    for j in crew:
        Application.objects.get_or_create(user=i, about=text, why=text, license="b", status=0, crew=j)



# population of events
dt = datetime.now()
for i in range(1,6):
    if (i == 5): # make one current event
        LanEvent.objects.get_or_create(name="Lan"+str(i), description="Lan nummer "+str(i), start_date=dt, end_date=dt, current=True)
    else:
        LanEvent.objects.get_or_create(name="Lan"+str(i), description="Lan nummer "+str(i), start_date=dt, end_date=dt, current=False)


# population of posts in news-app
users = ['thor','atle','anders','simen','bassan']
event = LanEvent.objects.all()
num = 3 # the two first posts are featured
for i in range(len(users)):
    for j in range(len(users)):
        user = SiteUser.objects.get(first_name=users[j])
        title = "Test "+str(num)
        num += 1 
        Post.objects.get_or_create(title=title, summary="SUMMARY "+text[:90], content="CONTENT "+text, author=SiteUser.get_user(user), slug=slugify(title), event=event[j])   
# Make two featured posts
for i in range(1,3):
    user = SiteUser.objects.get(first_name=users[i])
    title = "Test " + str(i)
    Post.objects.get_or_create(title=title, summary="FEATURED "+text[:90], content="CONTENT "+text, author=SiteUser.get_user(user), slug=slugify(title), event=event[4], featured=True)
