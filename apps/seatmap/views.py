from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from apps.seatmap.forms import CreateRowForm, CreateSeatmapForm
from apps.seatmap.models import Seatmap


@login_required
@user_passes_test(lambda u: u.is_chief())
def edit_seatmap(request, seatmap_id=None):
    seatmap = get_object_or_404(Seatmap, pk=seatmap_id)
    if request.POST:
        if request.is_ajax():
            form = CreateRowForm(request.POST)
            if form.is_valid():
                pass
            else:
                messages.error(request, "There was a problem, some information is not right")
        else:
            raise Http404

    form = CreateRowForm()

    return render(request, "seatmap/edit.html", {'form': form, 'seatmap': seatmap})