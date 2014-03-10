from django import forms

from apps.event.models import LanEvent
from apps.seatmap.models import Row


class CreateSeatmapForm(forms.Form):
    width = forms.IntegerField()
    height = forms.IntegerField()
    event = forms.ModelChoiceField(LanEvent)


class CreateRowForm(forms.Form):
    orientation = forms.ChoiceField(choices=Row.ORIENTATION)
    amount = forms.IntegerField()
    position_x = forms.IntegerField()
    position_z = forms.IntegerField()

