from django import forms
from core import models


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeedbackModel
        exclude = ("status",)


class NewsForm(forms.ModelForm):
    class Meta:
        model = models.NewsModel
        exclude = ("status",)


class NewsImageForm(forms.ModelForm):
    class Meta:
        model = models.NewsImages
        fields = ["image"]


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = models.BookmarkModel
        exclude = ("status",)
