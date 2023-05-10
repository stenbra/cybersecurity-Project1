from django.urls import path

from .views import homePageView, poemAddView,poemDetailView,poemDeleteView

urlpatterns = [
    path('', homePageView, name='home'),
    path('poems', poemAddView, name='addPoem'),
    path("poems/<int:poem_id>/", poemDetailView, name="poemDetails"),
    path("poems/<int:poem_id>/delete/", poemDeleteView, name="poemDelete"),
]
