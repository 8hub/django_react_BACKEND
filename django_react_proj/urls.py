from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/students/", views.StudentList.as_view()),
    path("api/students/<int:pk>/", views.StudentDetail.as_view()),
]
