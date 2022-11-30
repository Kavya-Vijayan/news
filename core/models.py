from django.db import models
from user.models import USER
from django.urls import reverse


class TimeStamp(models.Model):
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FeedbackModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.subject}"


class CategoryModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class NewsImages(models.Model):
    image = models.ImageField(upload_to="news/image/", default="default/news.png")


class NewsModel(TimeStamp, models.Model):
    heading = models.CharField(max_length=64)
    description = models.TextField(max_length=800)
    author = models.CharField(max_length=64)
    category = models.ManyToManyField(CategoryModel)
    image = models.ManyToManyField(NewsImages)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        url = reverse("core:news_detail", kwargs={"pk": self.id})
        return url


# Bookmark Model
class BookmarkModel(TimeStamp, models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.news}"
