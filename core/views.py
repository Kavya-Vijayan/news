from django import views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from core.forms import EducationForm, FeedbackForm, LateststoryForm, SportForm, TopstoryForm, TopwriterForm
from core import models as core_models
from django.views import generic as views


# home view
class HomeView(views.TemplateView):
    template_name = "core/home.html"
    extra_context={"lateststories":core_models.LateststoryModel.objects.all(),
                   "topstories":core_models.TopstoryModel.objects.all(),
                   "sports":core_models.SportModel.objects.all()}

#about usview
class AboutView(views.TemplateView):
     template_name = "core/about_us.html"


#====================================================================================================#
#                                           Feedback                                                 #
#====================================================================================================#

#feedback createview
class FeedbackCreateView(views.CreateView):
     template_name = "core/feedback/feedback_create.html"
     form_class = FeedbackForm
     success_url = reverse_lazy("core:feedback_create")

#feedback detailview
class FeedbackDetailView(views.DetailView):
     template_name = "core/feedback/feedback_detail.html"
     model= core_models.FeedbackModel

#feedback updateview
class FeedbackUpdateView(views.UpdateView):
     template_name = "core/feedback/feedback_update.html"
     form_class = FeedbackForm
     model= core_models.FeedbackModel
     success_url = reverse_lazy("core:feedback_list")

#feedback deleteview
class FeedbackDeleteView(views.DeleteView):
     template_name = "core/feedback/feedback_delete.html"
     form_class = FeedbackForm
     success_url = reverse_lazy("core:feedback_list")

#====================================================================================================#
#                                           Latest story                                             #
#====================================================================================================#

#lateststory createview
class LateststoryCreateView(views.CreateView):
    template_name = "core/lateststory/lateststory_create.html"
    form_class = LateststoryForm
    success_url = reverse_lazy("core:lateststory_create")

#lateststory listview
class LateststoryListView(views.ListView):
    template_name = "core/lateststory/lateststory_list.html"
    model = core_models.LateststoryModel
    context_object_name="lateststories"

#lateststory detailview
class LateststoryDetailView(views.DetailView):
    template_name = "core/lateststory/lateststory_detail.html"
    model = core_models.LateststoryModel
    context_object_name="lateststory"


#lateststory updateview
class LateststoryUpdateView(views.UpdateView):
    template_name = "core/lateststory/lateststory_update.html"
    model = core_models.LateststoryModel
    form_class =LateststoryForm
    success_url = reverse_lazy("core:lateststory_list")

#lateststory deleteview

class LateststoryDeleteView(views.DeleteView):
    template_name = "core/lateststory/lateststory_delete.html"
    model = core_models.LateststoryModel
    success_url = reverse_lazy("core:lateststory_list")

#====================================================================================================#
#                                           category                                                 #
#====================================================================================================#

#category listview
class CategoryListView(views.ListView):
    template_name = "core/category_list.html"
    model = core_models.CategoryModel
    context_object_name="categories"


#lateststory listview
class LateststoryByCategoryView(views.ListView):
    template_name = "core/lateststory/lateststory_list.html"
    model=core_models.LateststoryModel
    context_object_name="lateststories"
    def get_queryset(self,*args,**kwargs):
        qs=super().get_queryset(*args,**kwargs)
        pk=self.kwargs.get("pk",None)
        qs=qs.filter(category__id=pk)
        return qs


#topstory listview
class TopstoryByCategoryView(views.ListView):
    template_name = "core/topstory/topstory_list.html"
    model=core_models.TopstoryModel
    context_object_name="topstories"
    def get_queryset(self,*args,**kwargs):
        qs=super().get_queryset(*args,**kwargs)
        pk=self.kwargs.get("pk",None)
        qs=qs.filter(category__id=pk)
        return qs

 #====================================================================================================#
 #                                           Top story                                                #
 #====================================================================================================#

#topstory createview
class TopstoryCreateView(views.CreateView):
    template_name = "core/topstory/topstory_create.html"
    form_class = TopstoryForm
    success_url = reverse_lazy("core:topstory_create")

#topstory listview
class TopstoryListView(views.ListView):
    template_name = "core/topstory/topstory_list.html"
    model = core_models.TopstoryModel
    context_object_name="topstories"

#topstory detailview
class TopstoryDetailView(views.DetailView):
    template_name = "core/topstory/topstory_detail.html"
    model = core_models.TopstoryModel
    context_object_name="topstory"


#topstory updateview
class TopstoryUpdateView(views.UpdateView):
    template_name = "core/topstory/topstory_update.html"
    model = core_models.TopstoryModel
    form_class =TopstoryForm
    success_url = reverse_lazy("core:topstory_list")

#topstory deleteview

class TopstoryDeleteView(views.DeleteView):
    template_name = "core/topstory/topstory_delete.html"
    model = core_models.TopstoryModel
    success_url = reverse_lazy("core:topstory_list")




#====================================================================================================#
 #                                           Top writer                                              #
 #===================================================================================================#

#topwriter createview
class TopwriterCreateView(views.CreateView):
    template_name = "core/topwriter/topwriter_create.html"
    form_class = TopwriterForm
    success_url = reverse_lazy("core:topwriter_create")

#listview
class TopwriterListView(views.ListView):
    template_name = "core/topwriter/topwriter_list.html"
    model = core_models.TopwriterModel
    context_object_name="topwriters"

# detailview
class TopwriterDetailView(views.DetailView):
    template_name = "core/topwriter/topwriter_detail.html"
    model = core_models.TopwriterModel
    context_object_name="topwriters"


#updateview
class TopwriterUpdateView(views.UpdateView):
    template_name = "core/topwriter/topwriter_update.html"
    model = core_models.TopwriterModel
    form_class =TopwriterForm
    success_url = reverse_lazy("core:topwriter_list")

# deleteview

class TopwriterDeleteView(views.DeleteView):
    template_name = "core/topwriter/topwriter_delete.html"
    model = core_models.TopwriterModel
    success_url = reverse_lazy("core:topwriter_list")




#====================================================================================================#
#                                          Sports                                                    #
#====================================================================================================#

#sports createview
class SportCreateView(views.CreateView):
    template_name = "core/sport/sport_create.html"
    form_class = SportForm
    success_url = reverse_lazy("core:sport_create")

#sports listview
class SportListView(views.ListView):
    template_name = "core/sport/sport_list.html"
    model = core_models.SportModel
    context_object_name="sports"

#sports detailview
class SportDetailView(views.DetailView):
    template_name = "core/sport/sport_detail.html"
    model = core_models.SportModel
    context_object_name="sport"


#sports updateview
class SportUpdateView(views.UpdateView):
    template_name = "core/sport/sport_update.html"
    model = core_models.SportModel
    form_class =SportForm
    success_url = reverse_lazy("core:sport_list")

#sports deleteview

class SportDeleteView(views.DeleteView):
    template_name = "core/sport/sport_delete.html"
    model = core_models.SportModel
    success_url = reverse_lazy("core:sport_list")



#====================================================================================================#
#                                       Education                                                    #
#====================================================================================================#

#education createview
class EducationCreateView(views.CreateView):
    template_name = "core/education/education_create.html"
    form_class = EducationForm
    success_url = reverse_lazy("core:education_create")

#education listview
class EducationListView(views.ListView):
    template_name = "core/education/education_list.html"
    model = core_models.EducationModel
    context_object_name="educations"

#education detailview
class EducationDetailView(views.DetailView):
    template_name = "core/education/education_detail.html"
    model = core_models.EducationModel
    context_object_name="education"


#education updateview
class EducationUpdateView(views.UpdateView):
    template_name = "core/education/education_update.html"
    model = core_models.EducationModel
    form_class =EducationForm
    success_url = reverse_lazy("core:education_list")

#education deleteview

class EducationDeleteView(views.DeleteView):
    template_name = "core/education/education_delete.html"
    model = core_models.EducationModel
    success_url = reverse_lazy("core:education_list")


#-------------------------------------------------------------------------------------------#
#                                    local view                                             #
#-------------------------------------------------------------------------------------------#
class LocalView(views.TemplateView):
     template_name = "core/local.html"

#====================================================================================================#
#                                          cart                                                      #
#====================================================================================================#

class AddToBookmarkView(views.View):
    def get(self, request, pk):
        user = request.user
        lateststory = core_models.LateststoryModel.objects.get(id=pk)
        bookmark, bookmark_created = core_models.BookmarkModel.objects.get_or_create(
            user=user
        )
        bookmark_post, bookmark_post_created = core_models.BookmarkPostModel.objects.get_or_create(
            bookmark=bookmark, lateststory=lateststory
        )
        if not bookmark_post_created:
            bookmark_post.quantity += 1

        bookmark_post.save()
        url = request.META.get("HTTP_REFERER")
        return redirect(url)

