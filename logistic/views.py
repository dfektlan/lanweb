from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from logistic.models import ItemGroup, Item

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Core').count() == 1)
def index(request):
    items = Item.objects.all()
    return render(request, 'logistic/index.html', {'items':items})
