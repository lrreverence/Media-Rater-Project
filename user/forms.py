from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full mt-2 py-3 pl-10 pr-4 bg-slate-100 border border-slate-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent',
            'placeholder': 'Enter your email'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full mt-2 py-3 pl-10 pr-4 bg-slate-100 border border-slate-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent',
                'placeholder': 'Choose a username'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the default help text
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
        # Add styling to the password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full mt-2 py-3 pl-10 pr-4 bg-slate-100 border border-slate-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent',
            'placeholder': 'Choose a password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full mt-2 py-3 pl-10 pr-4 bg-slate-100 border border-slate-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent',
            'placeholder': 'Confirm password'
        })

    def save(self, commit=True):
        user = super(CustomerUserCreationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user