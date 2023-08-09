from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text', 'rating']
        widgets = {
            'feedback_text': forms.Textarea(attrs={'placeholder': 'Your feedback'}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }
