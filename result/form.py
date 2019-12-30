from django import forms
from result.models import CSE3101
from result.models import CSE3103
from result.models import CSE3105
from result.models import CSE3107
from result.models import CSE3109


class formcse_3101(forms.ModelForm):
    class Meta:
        model=CSE3101
        fields=['roll','ct1mark','ct2mark','ct3mark','ct4mark']

class formcse_3103(forms.ModelForm):
    class Meta:
        model=CSE3103
        fields=['roll','ct1mark','ct2mark','ct3mark','ct4mark']

class formcse_3105(forms.ModelForm):
    class Meta:
        model=CSE3105
        fields=['roll','ct1mark','ct2mark','ct3mark','ct4mark']

class formcse_3107(forms.ModelForm):
    class Meta:
        model=CSE3107
        fields=['roll','ct1mark','ct2mark','ct3mark','ct4mark']

class formcse_3109(forms.ModelForm):
    class Meta:
        model=CSE3109
        fields=['roll','ct1mark','ct2mark','ct3mark','ct4mark']
