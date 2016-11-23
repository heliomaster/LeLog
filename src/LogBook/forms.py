from django import forms
from .models import Logfields

class LogfieldsForm(forms.ModelForm):
    class Meta:
        model = Logfields
        fields = ["Date_field", "off_block_time"]