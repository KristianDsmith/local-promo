from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5)
    feedback = forms.CharField(widget=forms.Textarea)
    use_in_sets = forms.BooleanField(required=False)

    class Meta:
        model = Feedback
        fields = ['rating', 'feedback', 'use_in_sets']


class SignupForm(UserCreationForm):
    genre = forms.CharField(max_length=100, required=True)
    country = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
