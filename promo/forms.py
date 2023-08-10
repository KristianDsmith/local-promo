from django import forms
from .models import Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text', 'rating']
        widgets = {
            'feedback_text': forms.Textarea(attrs={'placeholder': 'Your feedback'}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
