from django import forms
from .models import Logfields
"""Toutes les forms du site sont dans ce fichier, si c'est un formulaire sans ref a la DB l'import est forms.froms
et si  la reference est la DB alors c'est forms.modelModelForm"""


class LogfieldsForm(forms.ModelForm):
    class Meta:
        model = Logfields
        fields = ["Date_field", "off_block_time", "take_off_time", "land_time", "on_block_time",
                  "tot_time_field", "pic_field", "fo_field", "dep_field", "arrival_field"]

# TODO: voir video "coding for entrepreuners" trydjango 12 of 42 pour form validation sur les dates et les heures
