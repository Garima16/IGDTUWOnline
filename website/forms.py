from django import forms
# from django.contrib.auth import authenticate
# from django_password_strength.widgets import PasswordStrengthInput,PasswordConfirmationInput


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            """
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user doesn't exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active")
            """

        return super(UserLoginForm, self).clean(*args, **kwargs)


class ChangePasswordForm(forms.Form):
    username = forms.CharField()
    new_password = forms.CharField(widget=forms.PasswordInput,
                                   help_text='Password should be atleast 8 characters long.\n'
                                             'Choose a password combination of atlesat an alphabet in both uppercase and lowercase,'
                                             'atleast 1 special character(#.^&*_@-) and a digit')
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       help_text='Type the same password as above')
