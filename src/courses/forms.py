from django import forms
from .models import Course


class CourseModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    content = forms.CharField(required=False,widget=forms.Textarea( attrs={"placeholder":"Your description","class":"new-class-name two","id":"my-id-for-textarea","rows":"20","columns":"120"}))
    #price = forms.DecimalField(initial='199.243')
    #email = forms.EmailField()
    class Meta:
        model = Course
        fields = [
            'title',
            'content',
        ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if  "CFE" not in title:
            raise forms.ValidationError("this is not a valid title")
        # elif  "NEWS" not in title:
        #     raise forms.ValidationError("this is not a valid title")

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



class RawCourseForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(required=False,widget=forms.Textarea( attrs={"placeholder":"Your description","class":"new-class-name two","id":"my-id-for-textarea","rows":"20","columns":"120"}))
    price = forms.DecimalField(initial='199.243')


