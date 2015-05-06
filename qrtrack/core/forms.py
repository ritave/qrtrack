from django import forms


class RegistrationForm(forms.Form):
    email = forms.CharField(label="Your e-mail", max_length=100)
    password = forms.CharField(label="Your password", max_length=30, widget=forms.PasswordInput)
    repeat_pass = forms.CharField(label="Repeat password", max_length=30,
                                  widget=forms.PasswordInput)
    wants_beta = forms.BooleanField(label="Do you want to be informed about beta?", required=False,
                                    initial=True)