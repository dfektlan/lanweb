from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.formsets import formset_factory
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
import pprint
import json

from apps.seatmap.models import Seatmap, Row, Seat


@login_required
@user_passes_test(lambda u: u.is_chief())
def edit_seatmap(request, seatmap_id=None):
    seatmap = get_object_or_404(Seatmap, pk=seatmap_id)
    rows = Row.objects.filter(seatmap=seatmap)
    dict = {"pk": seatmap_id, "height": seatmap.height, "width": seatmap.width, "rows": {}}
    for r in rows:
        dict["rows"][r.row] = {
            "position_x": r.position_x,
            "position_y": r.position_y,
            "orientation": r.orientation,
            "seats": {}
        }
        seats = Seat.objects.filter(row=r)

        for s in seats:
            dict["rows"][r.row]["seats"][s.number] = {
                "status": s.status
            }

    json_seatmap = json.dumps(dict)
    print json_seatmap

    return render(request, "seatmap/admin/edit.html", {'seatmap': seatmap, "json_seatmap": json_seatmap})


@login_required
@user_passes_test(lambda u: u.is_chief())
def save_seatmap(request):
    if request.is_ajax():
        data = json.loads(request.body)
        seatmap = Seatmap.objects.get(pk=data["pk"])

        #Adding and updateing
        for r in data["rows"]:
            row, created = Row.objects.get_or_create(seatmap=seatmap, row=r, defaults={
                "position_x": data["rows"][r]["position_x"],
                "position_y": data["rows"][r]["position_y"],
                "orientation": int(data["rows"][r]["orientation"]),
            })
            if not created:
                row.position_x = data["rows"][r]["position_x"]
                row.position_y = data["rows"][r]["position_y"]
                row.orientation = int(data["rows"][r]["orientation"])
                row.save()

            for s in data["rows"][r]["seats"]:
                seat, created = Seat.objects.get_or_create(row=row, number=s, defaults={
                    "status": data["rows"][r]["seats"][s]["status"]
                })
                if not created:
                    seat.status = data["rows"][r]["seats"][s]["status"]
                    seat.save()


        #Deleting

        rows = Row.objects.filter(seatmap=seatmap)
        for r in rows:
            if str(r.row) not in data["rows"].keys():
                r.delete()
            if str(r.row) in data["rows"].keys():
                seats = Seat.objects.filter(row=r)
                for s in seats:
                    if str(s.number) not in data["rows"][str(r.row)]["seats"]:
                        s.delete()



    return HttpResponse("OK")


@login_required
@user_passes_test(lambda u: u.is_chief())
def seat_overview(request, seatmap_id=None):
    seatmap = get_object_or_404(Seatmap, pk=seatmap_id)
    return render(request, "seatmap/admin/overview.html", {"seatmap": seatmap})
