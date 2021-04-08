from django import forms
from django.contrib.auth import get_user_model
from .models import UserStats, MyUser
from django.contrib.auth.forms import UserCreationForm

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length = 200)
    file = forms.FileField()
    
class SignUpForm(UserCreationForm):
    email = forms.CharField(required = True)
    quota = forms.IntegerField(required = True)
    
    class Meta:
        model = get_user_model()
        fields = ("username","password1","password2","email","quota")
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            UserStats(user_id = user.id, quota = self.cleaned_data["quota"]).save()
        return user, UserStats
        
    
    
