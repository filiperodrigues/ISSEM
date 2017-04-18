#coding:utf-8
from django import forms
from issem.models import CidModel


class CidForm(forms.ModelForm):
    filter = forms.ModelChoiceField(
        queryset=CidModel.objects.filter(excluido=0),
        widget=forms.Select(attrs={"class": "ui fluid search selection dropdown", })
    )

    class Meta:
        model = CidModel
        fields = '__all__'