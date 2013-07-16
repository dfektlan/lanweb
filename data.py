# -*- coding: utf-8 -*-
#from dfektlan import settings
from django.contrib.auth.models import Group
from userprofile.models import SiteUser
from crew.models import Application
from django.core.management import setup_environ
from news.models import Post
from django.template.defaultfilters import slugify

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

# population of posts in news-app
user = SiteUser.objects.all().filter(first_name='thor')
for i in range(1,30):
    title = "Test "+str(i)
    if ( i == 1 or i == 2 ):
        Post.objects.get_or_create(title=title, summary="FEATURED "+text[:90], content="CONTENT "+text, author=SiteUser.get_user(user[0]), slug=slugify(title), featured=True)
    else:
        Post.objects.get_or_create(title=title, summary="SUMMARY "+text[:90], content="CONTENT "+text, author=SiteUser.get_user(user[0]), slug=slugify(title))   
    



