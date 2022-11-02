from django.db import models
from user.models import USER

class FeedbackModel(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject}"

class CategoryModel(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class LateststoryModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to="lateststory/image/", default="default/lateststory.png")
    category = models.ManyToManyField(CategoryModel)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class TopstoryModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to="topstory/image/", default="default/topstory.png")
    category = models.ManyToManyField(CategoryModel)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class SportModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to="sport/image/", default="default/sport.png")
    category = models.ManyToManyField(CategoryModel)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"



class EducationModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=800)
    image = models.ImageField(upload_to="education/image/", default="default/education.png")
    category = models.ManyToManyField(CategoryModel)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


# Bookmark Model
class BookmarkModel(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def posts(self):
        bookmark_posts = BookmarkPostModel.objects.filter(
            bookmark=self,
            status=True,
        )
        return bookmark_posts

    def __str__(self):
        return f"{self.user}"


# Bookmark Post Model
class BookmarkPostModel(models.Model):
    bookmark = models.ForeignKey(BookmarkModel, on_delete=models.CASCADE)
    lateststory = models.ForeignKey(LateststoryModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lateststory}({self.quantity})"