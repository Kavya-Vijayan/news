from core import models as core_models


def common_data(request):
    user = request.user
    bookmark = None
    if user.is_authenticated:
        bookmark = core_models.BookmarkModel.objects.filter(user=user).last()
    context = {
        "bookmark": bookmark,
    }
    return context