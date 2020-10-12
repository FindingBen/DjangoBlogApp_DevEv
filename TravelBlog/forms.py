from django import forms as p_forms
from django.contrib.auth.models import Journey


class JourneyProfile(p_forms.ModelForm):
    class Meta:
        model = Journey
        fields = ('image')