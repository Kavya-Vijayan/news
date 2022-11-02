from django.contrib import admin
from core import models

admin.site.register(models.FeedbackModel)
admin.site.register(models.LateststoryModel)
admin.site.register(models.TopstoryModel)
admin.site.register(models.SportModel)
admin.site.register(models.EducationModel)
admin.site.register(models.CategoryModel)
admin.site.register(models.BookmarkModel)
admin.site.register(models.BookmarkPostModel)