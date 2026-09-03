from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search",views.search,name="search"),
    path("Add_page",views.Add_page,name="Add"),
    path("<str:title>",views.page)
]
