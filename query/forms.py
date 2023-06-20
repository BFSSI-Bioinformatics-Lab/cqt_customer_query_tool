from django import forms
from django.forms import ModelForm

from api.models import Query


class DateInput(forms.DateInput):
    input_type = 'date'


class QueryForm(forms.ModelForm):

    class Meta:
        model = Query
        fields = "__all__"
        widgets = {
            'date_due': forms.DateInput(attrs={'type': 'date'}),
            'date_BMH_received': forms.DateInput(attrs={'type': 'date'}),
            'date_assigned_to_evaluator': forms.DateInput(attrs={'type': 'date'}),
            'date_to_sections_head_for_approval': forms.DateInput(attrs={'type': 'date'}),
            'date_to_customer': forms.DateInput(attrs={'type': 'date'}),
        }
        
class UpdateQueryForm(forms.ModelForm):

    class Meta:
        model = Query
        fields = "__all__"
        widgets = {
            'date_due': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'date_BMH_received': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'date_assigned_to_evaluator': forms.DateInput(format=('%Y-%m-%d'), 
                                                          attrs={'type': 'date'}),
            'date_to_sections_head_for_approval': forms.DateInput(format=('%Y-%m-%d'), 
                                                                  attrs={'type': 'date'}),
            'date_to_customer': forms.DateInput(format=('%Y-%m-%d'), 
                                                attrs={'type': 'date'}),
        }