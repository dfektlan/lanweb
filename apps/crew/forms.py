from django.forms import ModelForm
from models import Application

class ApplicationAdminForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('user','about','why','license','date','cv') 
class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('status','date','user')

