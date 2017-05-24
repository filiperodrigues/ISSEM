# coding: utf-8
from django import forms
from issem.models import ParametrosConfiguracaoModel
from ckeditor.widgets import CKEditorWidget


class ParametrosConfiguracaoForm(forms.ModelForm):
    descricao_issem = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = ParametrosConfiguracaoModel
        fields = '__all__'
