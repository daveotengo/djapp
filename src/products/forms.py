from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(required=False,widget=forms.Textarea( attrs={"placeholder":"Your description","class":"new-class-name two","id":"my-id-for-textarea","rows":"20","columns":"120"}))
    price = forms.DecimalField(initial='199.243')
    email = forms.EmailField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("this is not a valid title")
        elif not "NEWS" in title:
            raise forms.ValidationError("this is not a valid title")

        else:
            return title

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        if not "edu" in email:
            raise forms.ValidationError("this is not a valid email")
        elif not "com" in title:
            raise forms.ValidationError("this is not a valid email")

        else:
            return email



class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(required=False,widget=forms.Textarea( attrs={"placeholder":"Your description","class":"new-class-name two","id":"my-id-for-textarea","rows":"20","columns":"120"}))
    price = forms.DecimalField(initial='199.243')


