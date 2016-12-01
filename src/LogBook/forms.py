from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=100)

from .models import Logfields

class LogfieldsForm(forms.ModelForm):
    class Meta:
        model = Logfields
        fields = ["Date_field", "off_block_time"]

