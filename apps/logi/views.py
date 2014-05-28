from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from apps.logi.forms import ItemForm
from apps.logi.models import Item
from apps.crew.models import Crew
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
@user_passes_test(lambda u: u.is_crew())
def item_overview(request, event=None):
    items = Item.objects.all()
    crews = Crew.objects.all()

    i = {}
    for crew in crews:
        i[crew] = filter(lambda x: x.owner == crew, items)

    return render(request, "logi/overview.html", {'items': i, 'event': event,})


def new_item(request, event=None, item_id=None):
    if item_id is None:
        item = Item()
    else:
        item = get_object_or_404(Item, pk=item_id)

    if request.POST:
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, u'Item successfully added')
            return redirect(item_overview)
        else:
            messages.error(request, u'Item unsuccessfully added')
    else:
        form = ItemForm()

    return render(request, "logi/form.html", {'form': form, 'event': event})
