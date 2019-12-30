from django import forms
from attendance.models import days

class formdays(forms.ModelForm):
    class Meta:
        model=days
        fields=['roll','classes']
