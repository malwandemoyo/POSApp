from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper

from .models import Category, InventoryItem

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

# class InventoryItemForm(forms.ModelForm):
# 	category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
#     def __init__(self, **args, **kwargs):
#         super().__init__(*args, **kwargs)        

#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.form_enctype = 'multipart/form-data'
    
# 	class Meta:
# 		model = InventoryItem
# 		fields = ['name', 'quantity', 'category', 'image', 'price']
  
# from crispy_forms.helper import FormHelper

class InventoryItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'

    class Meta:
        model = InventoryItem
        fields = "__all__"
        # fields = ['name', 'quantity', 'category', 'image', 'price']
