from django.urls import path

from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/result/", views.ResultsView.as_view(), name="result"),
    path("<int:pk>/vote/", views.voteView.as_view(), name="vote"),
]