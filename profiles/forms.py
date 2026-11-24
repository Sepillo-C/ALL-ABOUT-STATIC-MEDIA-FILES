from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'name',
            'bio',
            'location',
            'workplace',
            'school',
            'profile_picture',
            'cover_photo',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name'
            }),

            'bio': forms.Textarea(attrs={
                'placeholder': 'Write something about yourself',
                'rows': 3
            }),

            'location': forms.TextInput(attrs={
                'placeholder': 'Your location'
            }),

            'workplace': forms.TextInput(attrs={
                'placeholder': 'Where do you work?'
            }),

            'school': forms.TextInput(attrs={
                'placeholder': 'Your school'
            }),
        }
