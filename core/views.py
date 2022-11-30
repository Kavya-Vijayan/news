from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from core import models as core_models
from core.forms import FeedbackForm


# home view
class HomeView(views.TemplateView):
    template_name = "core/home.html"


# about usview
class AboutView(views.TemplateView):
    template_name = "core/about_us.html"


# ====================================================================================================#
#                                           Feedback                                                  #
# ====================================================================================================#

# feedback createview
class FeedbackCreateView(views.CreateView):
    template_name = "core/feedback/feedback_create.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("core:feedback_create")


# feedback detailview
class FeedbackDetailView(views.DetailView):
    template_name = "core/feedback/feedback_detail.html"
    model = core_models.FeedbackModel


# feedback updateview
class FeedbackUpdateView(views.UpdateView):
    template_name = "core/feedback/feedback_update.html"
    form_class = FeedbackForm
    model = core_models.FeedbackModel
    success_url = reverse_lazy("core:feedback_list")


# feedback deleteview
class FeedbackDeleteView(views.DeleteView):
    template_name = "core/feedback/feedback_delete.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("core:feedback_list")


# ====================================================================================================#
#                                           News                                                      #
# ====================================================================================================#

# news createview
class NewsListView(views.ListView):
    template_name = "core/news/news_list.html"
    model = core_models.NewsModel
    context_object_name = "news_list"
    ordering = "-updated_on"


# news listview
class NewsDetailView(views.DetailView):
    template_name = "core/news/news_detail.html"
    model = core_models.NewsModel
    context_object_name = "news"


# ====================================================================================================#
#                                           category                                                  #
# ====================================================================================================#

# category listview
class CategoryListView(views.ListView):
    template_name = "core/category/category_list.html"
    model = core_models.CategoryModel
    context_object_name = "categories"


# news by category listview
class NewsByCategoryView(views.ListView):
    template_name = "core/news/news_list.html"
    model = core_models.NewsModel
    context_object_name = "news_list"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        pk = self.kwargs.get("pk", None)
        qs = qs.filter(category__id=pk)
        return qs

# ====================================================================================================#
#                                           Dashboard                                                 #
# ====================================================================================================#


class DashboardView(views.TemplateView):
    template_name = "core/dashboard_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add extra context data here
        # context[""] =
        return context


# ====================================================================================================#
#                                          Bookmark                                                   #
# ====================================================================================================#
class BookmarkListView(views.View):
    template_name = "core/bookmark/bookmark_list.html"
    model = core_models.BookmarkModel
    context_object_name = "bookmarks"


class AddToBookmarkView(views.View):
    def get(self, request, pk):
        user = request.user
        news = core_models.NewsModel.objects.get(id=pk)
        bookmark, bookmark_created = core_models.BookmarkModel.objects.get_or_create(
            user=user,
            news=news,
        )

        if bookmark_created:
            messages.success(request, "Bokkmark added successfully!")
        else:
            messages.info(request, "Already bookmarked!")

        url = request.META.get("HTTP_REFERER")
        return redirect(url)


class RemoveFromBookmarkView(views.View):
    def get(self, request, pk):
        try:
            bookmark = core_models.BookmarkModel.objects.get(id=pk)
            bookmark.delete()
            messages.success(request, "Bookmark removed successfully!")
        except:
            messages.info(request, "Can not remove right now! Please try again later!")
        url = request.META.get("HTTP_REFERER")
        return redirect(url)

# ====================================================================================================#
#                                          Search                                                     #
# ====================================================================================================#

class NewsSearchView(views.ListView):
    template_name = "core/news/news_list.html"
    model = core_models.NewsModel
    context_object_name = "news_list"
    ordering = "-updated_on"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q", None)
        qs = qs.filter(Q(name__icontains=q) | Q(category__name__icontains=q))
        return qs
