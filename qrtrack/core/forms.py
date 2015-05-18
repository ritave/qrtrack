from django import forms
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.translation import ugettext as _

class RegistrationForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=100, required=True)
    email = forms.CharField(label=_("Your e-mail (optional)"), max_length=100, required=False)
    password = forms.CharField(label=_("Your password"), max_length=30, widget=forms.PasswordInput,
                               required=True)
    repeat_pass = forms.CharField(label=_("Repeat password"), max_length=30, required=True,
                                  widget=forms.PasswordInput)
    wants_beta = forms.BooleanField(label=_("Do you want to be informed about beta?"), required=False,
                                    initial=True)

    def clean(self):
        cleaned = super(RegistrationForm, self).clean()

        wants_beta = cleaned.get('wants_beta')
        email = cleaned.get('email')
        username = cleaned.get('username')
        if wants_beta and email == '':
            raise forms.ValidationError(_("You need email to be informed about beta"))

        if email == '':
            email_q = Q()
        else:
            email_q = Q(email=email)
        if User.objects.filter(email_q | Q(username=username)).exists():
            raise forms.ValidationError(_("User with this email or username already exists"))

        pass1 = cleaned.get('password')
        pass2 = cleaned.get('repeat_pass')
        if pass1 != pass2:
            raise forms.ValidationError(_("The passwords don't match"))
        return cleaned
