from django.urls import path

# from . import views
from .views import drink_id, drink_list

urlpatterns = [
    path("drinks/", drink_list.as_view(), name="drink_list"),
    path("drinks/<int:id>", drink_id.as_view(), name="drink_id"),
]
