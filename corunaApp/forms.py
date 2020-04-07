from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'class':'message-box'}), required=True)
    
    