from django import forms
from .models import Plant


class DateInput(forms.DateInput):
    input_type = 'date'


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'text', 'watering_frequency', 'watering_date', 'image']
        labels = {'name': 'Name', 'text': 'Description / Useful information',
                  'watering_frequency': 'How often you should water this plant?',
                  'watering_date': 'Last watering date'}
        widgets = {
            'watering_date': DateInput()
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'text', 'watering_frequency', 'image']
        labels = {'name': 'Name', 'text': 'Description / Useful information',
                  'watering_frequency': 'Watering frequency'}
