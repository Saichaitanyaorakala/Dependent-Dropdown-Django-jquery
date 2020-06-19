from django.forms import ModelForm
from django import forms
from .models import Employee


exec_choice = [
('yes','Yes'),
('no','No'),
]

payment_choice = [
('PAD', 'Pre-Authorized Debit'),
('cheque','Cheque'),
]

class EmployeeForm(ModelForm):
    executive_authority = forms.ChoiceField(choices=exec_choice, widget=forms.RadioSelect())
    payment_type = forms.ChoiceField(choices=payment_choice, widget=forms.RadioSelect())
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter your Title/Position ', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control'}),
            'fax': forms.TextInput(attrs={'placeholder': 'Enter Fax number', 'class': 'form-control'}),
            'executive_authority': forms.RadioSelect(attrs={'class': 'form-control'}),
            'exec_first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'}),
            'exec_last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'}),
            'exec_title': forms.TextInput(attrs={'placeholder': 'Enter your Title/Position ', 'class': 'form-control'}),
            'exec_email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'exec_phone_number': forms.NumberInput(attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control'}),
            'exec_fax': forms.TextInput(attrs={'placeholder': 'Enter Fax number', 'class': 'form-control'}),
            }
