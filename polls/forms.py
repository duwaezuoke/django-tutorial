from django import forms

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)
    
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, 
                               widget=forms.Textarea)