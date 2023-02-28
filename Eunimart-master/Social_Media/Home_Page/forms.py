from django import forms


class user_cred(forms.Form):
    first_name=forms.CharField(max_length=50)
    middle_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    phone_number=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=10000,widget=forms.PasswordInput)

class login_validate(forms.Form):
    emails=forms.EmailField()
    passwords=forms.CharField(max_length=1000,widget=forms.PasswordInput)

class post_tweet(forms.Form):
    user_tweet = forms.CharField(widget=forms.Textarea)
