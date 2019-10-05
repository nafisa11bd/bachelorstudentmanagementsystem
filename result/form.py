from django import forms
from result.models import CSE3101

class formcse_3101(forms.ModelForm):
    class Meta:
        model=CSE3101
        fields=['roll','ct1mark','ct2mark','ct3mark','ct4mark']
