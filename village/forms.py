from django import forms
from .models import Reservation
from datetime import date

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'visit_date', 'number_of_visitors', 'need_guide', 'special_requests']
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}),
            'special_requests': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        self.destination = kwargs.pop('destination', None)
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.destination = self.destination
        instance.total_price = instance.calculate_price()
        
        if commit:
            instance.save()
        return instance 