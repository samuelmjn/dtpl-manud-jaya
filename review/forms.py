from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the rating field required
        self.fields['rating'].required = True
        # We're not using the widget's rendering, but set choices for validation
        self.fields['rating'].choices = [
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars')
        ]
        # Customize the comment field
        self.fields['comment'].widget = forms.Textarea(
            attrs={'class': 'form-control', 'cols': 50, 'rows': 5}
        )

    def save(self, commit=True):
        form = super().save(commit=False)
        form.is_used = True

        if commit:
            form.save()
        return form