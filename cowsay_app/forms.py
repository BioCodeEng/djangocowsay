from django import forms
import subprocess

# Create your forms here.
class CowForm(forms.Form):
    text = forms.CharField(max_length=135)
