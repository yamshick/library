from django.urls import path

from . import views

# app_name = "book"
urlpatterns = [
    # ex: /book/
    path("", views.index, name="index"),
    # ex: /book/5/
    path("<int:book_id>/", views.detail, name="detail"),
]