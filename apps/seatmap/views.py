from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.formsets import formset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from apps.seatmap.forms import CreateRowForm, CreateSeatmapForm
from apps.seatmap.models import Seatmap, Row, Seat


@login_required
@user_passes_test(lambda u: u.is_chief())
def edit_seatmap(request, seatmap_id=None):
    seatmap = get_object_or_404(Seatmap, pk=seatmap_id)
    createRowFormSet = formset_factory(CreateRowForm)
    if request.POST:
        if request.POST:
            formset = createRowFormSet(request.POST)
            if formset.is_valid():
                if Row.objects.filter(seatmap=seatmap).count() == 0:
                    print 'merp'
                    for form in formset:
                        row = Row()
                        row.row = form.cleaned_data["rownumber"]
                        row.orientation = form.cleaned_data["orientation"]
                        row.position_x = form.cleaned_data["position_x"]
                        row.position_y = form.cleaned_data["position_y"]
                        row.seatmap = seatmap
                        row.save()
                        for s in range(1, form.cleaned_data["amount"] + 1):
                            seat = Seat()
                            seat.status = 0
                            seat.row = row
                            seat.number = s
                            seat.save()


            else:
                messages.error(request, "There was a problem, some information is not right")
        else:
            raise Http404

    formset = createRowFormSet()

    return render(request, "seatmap/edit.html", {'formset': formset, 'seatmap': seatmap})