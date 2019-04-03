from django import forms

from .models import To

class ToForm(forms.ModelForm):

	class Meta:
		model = To
		fields = ('todo', 'action',)