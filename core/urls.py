from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("about/",views.AboutView.as_view(),name="about_us"),
    path("search/",views.SearchView.as_view(),name="search"),
    path("local/",views.LocalView.as_view(),name="local"),
    
    # lateststory
    path("lateststory/list/",views.LateststoryListView.as_view(),name="lateststory_list"),
    path("lateststory/create",views.LateststoryCreateView.as_view(),name="lateststory_create"),
    path("lateststory/<int:pk>/detail/",views.LateststoryDetailView.as_view(),name="lateststory_detail"),
    path("lateststory/<int:pk>/update/",views.LateststoryUpdateView.as_view(),name="lateststory_update"),
    path("lateststory/<int:pk>/delete/",views.LateststoryDeleteView.as_view(),name="lateststory_delete"),

    # topstory
    path("topstory/list/",views.TopstoryListView.as_view(),name="topstory_list"),
    path("topstory/create",views.TopstoryCreateView.as_view(),name="topstory_create"),
    path("topstory/<int:pk>/detail/",views.TopstoryDetailView.as_view(),name="topstory_detail"),
    path("topstory/<int:pk>/update/",views.TopstoryUpdateView.as_view(),name="topstory_update"),
    path("topstory/<int:pk>/delete/",views.TopstoryDeleteView.as_view(),name="topstory_delete"),

    # topwriter
    path("topwriter/list/",views.TopwriterListView.as_view(),name="topwriter_list"),
    path("topwriter/create",views.TopwriterCreateView.as_view(),name="topwriter_create"),
    path("topwriter/<int:pk>/detail/",views.TopwriterDetailView.as_view(),name="topwriter_detail"),
    path("topwriter/<int:pk>/update/",views.TopwriterUpdateView.as_view(),name="topwriter_update"),
    path("topwriter/<int:pk>/delete/",views.TopwriterDeleteView.as_view(),name="topwriter_delete"),


    # sports
    path("sport/list/",views.SportListView.as_view(),name="sport_list"),
    path("sport/create",views.SportCreateView.as_view(),name="sport_create"),
    path("sport/<int:pk>/detail/",views.SportDetailView.as_view(),name="sport_detail"),
    path("sport/<int:pk>/update/",views.SportUpdateView.as_view(),name="sport_update"),
    path("sport/<int:pk>/delete/",views.SportDeleteView.as_view(),name="sport_delete"),


    # education
    path("education/list/",views.EducationListView.as_view(),name="education_list"),
    path("education/create",views.EducationCreateView.as_view(),name="education_create"),
    path("education/<int:pk>/detail/",views.EducationDetailView.as_view(),name="education_detail"),
    path("education/<int:pk>/update/",views.EducationUpdateView.as_view(),name="education_update"),
    path("education/<int:pk>/delete/",views.EducationDeleteView.as_view(),name="education_delete"),


    # feedback
    path("feedback/create",views.FeedbackCreateView.as_view(),name="feedback_create"),
    path("feedback/<int:pk>/detail/",views.FeedbackDetailView.as_view(),name="feedback_detail"),
    path("feedback/<int:pk>/update/",views.FeedbackUpdateView.as_view(),name="feedback_update"),
    path("feedback/<int:pk>/delete/",views.FeedbackDeleteView.as_view(),name="feedback_delete"),
    #category
    path("category/list",views.CategoryListView.as_view(),name="category_list"),

    #lateststory list
    path("lateststory_by_category/<int:pk>/list/",views.LateststoryByCategoryView.as_view(),name="lateststory_by_category"),
       
    #topstory list
    path("topstory_by_category/<int:pk>/list/",views.TopstoryByCategoryView.as_view(),name="topstory_by_category"),



    #bookmark
    path("bookmark/lateststory/<int:pk>/add/",views.AddToBookmarkView.as_view(), name="add_to_bookmark"),

    #profile
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("dashboard/",views.DashboardView.as_view(),name="dashboard"),
    path("forgot/",views.ForgotView.as_view(),name="forgot"),
    
]