from django import forms

from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'text', 'watering_frequency', 'watering_date']
        labels = {'name': 'Name', 'text': 'Description / Useful information', 'watering_frequency': 'How often you should water this plant?',
                  'watering_date': 'Last watering date'}
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'text', 'watering_frequency']
        labels = {'name': 'Name', 'text': 'Description / Useful information', 'watering_frequency': 'Watering frequency'}