from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback
from .models import UserProfile


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text', 'rating']
        widgets = {
            'feedback_text': forms.Textarea(attrs={'placeholder': 'Your feedback'}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }


class SignupForm(UserCreationForm):
    genre = forms.CharField(max_length=100, required=True)
    country = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
