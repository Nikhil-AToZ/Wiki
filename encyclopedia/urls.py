from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search",views.search,name="search"),
    path("Add_page",views.Add_page,name="Add"),
    path("edit/<str:title>",views.edit_page,name="edit"),
    path("<str:title>",views.page)
]
