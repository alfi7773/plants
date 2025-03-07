from django import forms
from .models import Region

class AddressForm(forms.Form):
    country = CountryField().formfield()
    region = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].choices = [("", "Выберите страну сначала")]