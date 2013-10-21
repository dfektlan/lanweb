from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from apps.logistic.models import ItemGroup, Item
from apps.logistic.forms import ItemForm
from apps.userprofile.models import SiteUser


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Core').count() == 1)
def index(request):
    items = Item.objects.all()
    forms = []
    if request.POST:
        print request.POST
        print request.POST.getlist('id')
        post = zip(request.POST.getlist("id"),request.POST.getlist("holder"))
        print post
        for idd,holder in post:
            item = Item.objects.get(id=idd)
            try:
                item.holder = SiteUser.objects.get(id=holder)
            except ValueError:
                item.holder = None
            item.save()
        return redirect('/logistic')
    else: 
        for i in items:
            forms.append(ItemForm(instance=i))
        
    both = zip(items, forms)
    return render(request, 'logistic/index.html', {'items':items, 'forms':forms, 'both':both})

