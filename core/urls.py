from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("about/",views.AboutView.as_view(),name="about_us"),
   # news
    path("news/list/",views.NewsListView.as_view(),name="news_list"),
    path("news/<int:pk>/detail/",views.NewsDetailView.as_view(),name="news_detail"),
    # feedback
    path("feedback/create",views.FeedbackCreateView.as_view(),name="feedback_create"),
    path("feedback/<int:pk>/detail/",views.FeedbackDetailView.as_view(),name="feedback_detail"),
    path("feedback/<int:pk>/update/",views.FeedbackUpdateView.as_view(),name="feedback_update"),
    path("feedback/<int:pk>/delete/",views.FeedbackDeleteView.as_view(),name="feedback_delete"),
    #category
    path("category/list/",views.CategoryListView.as_view(),name="category_list"),
    #bookmark
    path("bookmark/add/news/<int:pk>/",views.AddToBookmarkView.as_view(), name="add_to_bookmark"),
    path("bookmark/remove/<int:pk>/",views.RemoveFromBookmarkView.as_view(), name="remove_from_bookmark"),
    #dashboard
    path("dashboard/",views.DashboardView.as_view(),name="dashboard"),
    #search
    path("category/search/",views.NewsByCategoryView.as_view(),name="category_search"),
]