from django.urls import path

# from . import views
from .views import task_item, task_list


urlpatterns = [
    path("tasks/", task_list.as_view(), name="task_list"),
    path("tasks/<int:id>", task_item.as_view(), name="task_id"),
]
