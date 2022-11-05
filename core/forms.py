from django import forms
from core import models
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.FeedbackModel
        # fields="__all__" #["name","message","email"]
        exclude=('status',)

class LateststoryForm(forms.ModelForm):
    class Meta:
        model=models.LateststoryModel
        # fields="__all__" #["name","message","email"]
        exclude=('status','created_on','updated_on',)

class TopstoryForm(forms.ModelForm):
    class Meta:
        model=models.TopstoryModel
        # fields="__all__" #["name","message","email"]
        exclude=('status','created_on','updated_on',)

class TopwriterForm(forms.ModelForm):
    class Meta:
        model=models.TopwriterModel
        # fields="__all__" #["name","message","email"]
        exclude=('status','created_on','updated_on',)


class SportForm(forms.ModelForm):
    class Meta:
        model=models.SportModel
        # fields="__all__" #["name","message","email"]
        exclude=('status','created_on','updated_on',)


class EducationForm(forms.ModelForm):
    class Meta:
        model=models.EducationModel
        # fields="__all__" #["name","message","email"]
        exclude=('status','created_on','updated_on',)