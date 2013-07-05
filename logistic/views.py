from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from logistic.models import ItemGroup, Item
from logistic.forms import ItemForm

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Core').count() == 1)
def index(request):
    items = Item.objects.all()
    forms = []
    if request.POST:
        print request.POST
        print request.POST["id"]
        print Item.objects.get(id=request.POST["id"])
        form = ItemForm(request.POST, instance=Item.objects.get(id=request.POST["id"][0]))
        forms.append(form)
        if form.is_valid():
           form.save()
        return redirect('/logistic')
    else: 
        for i in items:
            forms.append(ItemForm(instance=i))
        
    both = zip(items, forms)
    return render(request, 'logistic/index.html', {'items':items, 'forms':forms, 'both':both})
