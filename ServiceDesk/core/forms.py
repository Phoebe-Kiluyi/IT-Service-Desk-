from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Ticket, Feedback, CustomUser

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'category', 'due_date', 'attachment']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'priority': forms.Select(choices=Ticket.PRIORITY_CHOICES),
            'category': forms.Select(choices=Ticket.CATEGORY_CHOICES),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'attachment': forms.FileInput(),
        }

class FeedbackForm(forms.ModelForm):
    ticket = forms.ModelChoiceField(queryset=Ticket.objects.all(), empty_label="Select a Ticket")
    
    class Meta:
        model = Feedback
        fields = ['ticket', 'user_name', 'user_email', 'message', 'rating']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    # Additional fields if needed
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
