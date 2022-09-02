from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name = "starting-page"),
    path("posts", views.AllPostsView.as_view(), name = "posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name = "post-detail-page")#/posts/my-first-post this way of specifying is called slug. That does not mean the <slug> needs to be so, it could be any name.
]

# Here views.posts calles the post function in the views file and name is simply a name given to this particular path. This goes for all the paths mentioned in this file. 